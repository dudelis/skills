"""Tests for prepare_image.py, run from this folder: python -m unittest test_prepare_image"""

from __future__ import annotations

import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from PIL import Image

import prepare_image

BRIEF = '---\nhandle: "resens-augen-handpflege"\nstatus: "awaiting-image"\n---\n\n# Slide\n'


def make_folder(tmp: str) -> Path:
    folder = Path(tmp) / "2026-11-02-resens-augen-handpflege"
    folder.mkdir()
    (folder / "brief.md").write_text(BRIEF, encoding="utf-8")
    return folder


def run(*argv: str) -> tuple[int, str]:
    out = io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
        code = prepare_image.main(list(argv))
    return code, out.getvalue()


class PrepareImageTest(unittest.TestCase):
    def test_wide_png_becomes_handle_png_at_1536x1024(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            folder = make_folder(tmp)
            Image.new("RGB", (3000, 1500), "white").save(folder / "ChatGPT Image.png")

            code, _ = run(str(folder))

            self.assertEqual(code, 0)
            with Image.open(folder / "resens-augen-handpflege.png") as result:
                self.assertEqual(result.size, (1536, 1024))
                self.assertEqual(result.format, "PNG")

    def test_jpg_and_webp_keep_their_format(self) -> None:
        for source_name, expected_name, expected_format in [
            ("gemini.jpeg", "resens-augen-handpflege.jpg", "JPEG"),
            ("gemini.webp", "resens-augen-handpflege.webp", "WEBP"),
        ]:
            with self.subTest(source_name), tempfile.TemporaryDirectory() as tmp:
                folder = make_folder(tmp)
                Image.new("RGB", (1024, 1024), "white").save(folder / source_name)

                code, _ = run(str(folder))

                self.assertEqual(code, 0)
                with Image.open(folder / expected_name) as result:
                    self.assertEqual(result.size, (1536, 1024))
                    self.assertEqual(result.format, expected_format)

    def test_svg_is_refused_with_a_warning(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            folder = make_folder(tmp)
            (folder / "slide.svg").write_text("<svg xmlns='http://www.w3.org/2000/svg'/>", encoding="utf-8")

            code, output = run(str(folder))

            self.assertNotEqual(code, 0)
            self.assertIn("SVG", output)
            self.assertEqual(sorted(p.name for p in folder.iterdir()), ["brief.md", "slide.svg"])

    def test_explicit_svg_gets_the_svg_warning(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            folder = make_folder(tmp)
            svg = Path(tmp) / "logo.svg"
            svg.write_text("<svg xmlns='http://www.w3.org/2000/svg'/>", encoding="utf-8")

            code, output = run(str(folder), "--image", str(svg))

            self.assertNotEqual(code, 0)
            self.assertIn("probably a mistake", output)

    def test_svg_next_to_a_raster_image_is_reported_as_ignored(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            folder = make_folder(tmp)
            (folder / "draft.svg").write_text("<svg xmlns='http://www.w3.org/2000/svg'/>", encoding="utf-8")
            Image.new("RGB", (1536, 1024), "white").save(folder / "slide.png")

            code, output = run(str(folder))

            self.assertEqual(code, 0)
            self.assertIn("draft.svg", output)
            self.assertTrue((folder / "resens-augen-handpflege.png").exists())

    def test_missing_or_ambiguous_image_asks_for_a_path(self) -> None:
        for names in [[], ["one.png", "two.jpg"]]:
            with self.subTest(names=names), tempfile.TemporaryDirectory() as tmp:
                folder = make_folder(tmp)
                for name in names:
                    Image.new("RGB", (1536, 1024), "white").save(folder / name)

                code, output = run(str(folder))

                self.assertNotEqual(code, 0)
                self.assertIn("--image", output)

    def test_rerun_ignores_the_already_processed_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            folder = make_folder(tmp)
            Image.new("RGB", (2048, 2048), "white").save(folder / "original.png")
            self.assertEqual(run(str(folder))[0], 0)

            code, _ = run(str(folder))

            self.assertEqual(code, 0)
            with Image.open(folder / "resens-augen-handpflege.png") as result:
                self.assertEqual(result.size, (1536, 1024))

    def test_explicit_image_path_is_written_into_the_folder(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            folder = make_folder(tmp)
            outside = Path(tmp) / "Downloads" / "generated.jpg"
            outside.parent.mkdir()
            Image.new("RGB", (1920, 1080), "white").save(outside)

            code, _ = run(str(folder), "--image", str(outside))

            self.assertEqual(code, 0)
            with Image.open(folder / "resens-augen-handpflege.jpg") as result:
                self.assertEqual(result.size, (1536, 1024))

    def test_small_source_warns_about_upscaling(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            folder = make_folder(tmp)
            Image.new("RGB", (1024, 1024), "white").save(folder / "small.png")

            code, output = run(str(folder))

            self.assertEqual(code, 0)
            self.assertIn("upscaled", output)

    def test_large_source_has_no_upscaling_warning(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            folder = make_folder(tmp)
            Image.new("RGB", (1536, 1024), "white").save(folder / "exact.png")

            _, output = run(str(folder))

            self.assertNotIn("upscaled", output)


if __name__ == "__main__":
    unittest.main()
