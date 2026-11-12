"""Tests for prepare_image.py, run from this folder: python -m unittest test_prepare_image"""

from __future__ import annotations

import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from PIL import Image

import prepare_image

BRIEF = '---\nhandle: "resens-augen-handpflege"\nstatus: "awaiting-images"\n---\n\n# Slide\n'


def make_folder(tmp: str) -> Path:
    folder = Path(tmp) / "2026-11-02-resens-augen-handpflege"
    folder.mkdir()
    (folder / "brief.md").write_text(BRIEF, encoding="utf-8")
    return folder


def add_desktop(folder: Path, size: tuple[int, int] = (1536, 1024), name: str = "desktop.png") -> None:
    Image.new("RGB", size, "white").save(folder / name)


def add_mobile(folder: Path, size: tuple[int, int] = (1536, 864)) -> None:
    Image.new("RGB", size, "white").save(folder / "generated-mobile.png")


def run(*argv: str) -> tuple[int, str]:
    out = io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
        code = prepare_image.main(list(argv))
    return code, out.getvalue()


class PrepareImageTest(unittest.TestCase):
    def test_desktop_and_mobile_sources_become_both_slide_images(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            folder = make_folder(tmp)
            add_desktop(folder)
            add_mobile(folder, (1672, 941))

            code, _ = run(str(folder))

            self.assertEqual(code, 0)
            with Image.open(folder / "resens-augen-handpflege.png") as desktop:
                self.assertEqual(desktop.size, (1536, 1024))
            with Image.open(folder / "resens-augen-handpflege-mobile.png") as mobile:
                self.assertEqual(mobile.size, (1536, 864))

    def test_missing_mobile_source_fails_and_names_the_suffix(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            folder = make_folder(tmp)
            add_desktop(folder)

            code, output = run(str(folder))

            self.assertNotEqual(code, 0)
            self.assertIn("-mobile", output)
            self.assertEqual(sorted(p.name for p in folder.iterdir()), ["brief.md", "desktop.png"])

    def test_missing_desktop_source_fails_and_writes_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            folder = make_folder(tmp)
            add_mobile(folder)

            code, output = run(str(folder))

            self.assertNotEqual(code, 0)
            self.assertIn("desktop image", output)
            self.assertEqual(sorted(p.name for p in folder.iterdir()), ["brief.md", "generated-mobile.png"])

    def test_portrait_mobile_source_warns_about_the_crop(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            folder = make_folder(tmp)
            add_desktop(folder)
            add_mobile(folder, (1024, 1536))

            code, output = run(str(folder))

            self.assertEqual(code, 0)
            self.assertIn("generated-mobile.png", output)
            self.assertIn("crop", output)

    def test_landscape_mobile_sources_have_no_crop_warning(self) -> None:
        # 1672x941 is a generator's 16:9; 1536x1024 is ChatGPT's only landscape size.
        for size in [(1672, 941), (1536, 1024)]:
            with self.subTest(size=size), tempfile.TemporaryDirectory() as tmp:
                folder = make_folder(tmp)
                add_desktop(folder)
                add_mobile(folder, size)

                _, output = run(str(folder))

                self.assertNotIn("crop", output)

    def test_wide_png_becomes_handle_png_at_1536x1024(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            folder = make_folder(tmp)
            add_desktop(folder, (3000, 1500), "ChatGPT Image.png")
            add_mobile(folder)

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
                add_desktop(folder, name=source_name)
                add_mobile(folder)

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
            add_desktop(folder, name="slide.png")
            add_mobile(folder)

            code, output = run(str(folder))

            self.assertEqual(code, 0)
            self.assertIn("draft.svg", output)
            self.assertTrue((folder / "resens-augen-handpflege.png").exists())

    def test_missing_or_ambiguous_image_asks_for_a_path(self) -> None:
        for names in [[], ["one.png", "two.jpg"]]:
            with self.subTest(names=names), tempfile.TemporaryDirectory() as tmp:
                folder = make_folder(tmp)
                for name in names:
                    add_desktop(folder, name=name)
                add_mobile(folder)

                code, output = run(str(folder))

                self.assertNotEqual(code, 0)
                self.assertIn("--image", output)

    def test_rerun_ignores_both_processed_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            folder = make_folder(tmp)
            add_desktop(folder, (2048, 1365), "original.png")
            add_mobile(folder, (1920, 1080))
            self.assertEqual(run(str(folder))[0], 0)

            code, _ = run(str(folder))

            self.assertEqual(code, 0)
            with Image.open(folder / "resens-augen-handpflege.png") as desktop:
                self.assertEqual(desktop.size, (1536, 1024))
            with Image.open(folder / "resens-augen-handpflege-mobile.png") as mobile:
                self.assertEqual(mobile.size, (1536, 864))

    def test_explicit_image_paths_are_written_into_the_folder(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            folder = make_folder(tmp)
            downloads = Path(tmp) / "Downloads"
            downloads.mkdir()
            Image.new("RGB", (1920, 1280), "white").save(downloads / "generated.jpg")
            Image.new("RGB", (1920, 1080), "white").save(downloads / "wide.jpg")

            code, _ = run(
                str(folder), "--image", str(downloads / "generated.jpg"), "--mobile-image", str(downloads / "wide.jpg")
            )

            self.assertEqual(code, 0)
            with Image.open(folder / "resens-augen-handpflege.jpg") as desktop:
                self.assertEqual(desktop.size, (1536, 1024))
            with Image.open(folder / "resens-augen-handpflege-mobile.jpg") as mobile:
                self.assertEqual(mobile.size, (1536, 864))

    def test_small_source_warns_about_upscaling(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            folder = make_folder(tmp)
            add_desktop(folder, (1024, 683), "small.png")
            add_mobile(folder)

            code, output = run(str(folder))

            self.assertEqual(code, 0)
            self.assertIn("upscaled", output)

    def test_large_source_has_no_upscaling_warning(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            folder = make_folder(tmp)
            add_desktop(folder, name="exact.png")
            add_mobile(folder)

            _, output = run(str(folder))

            self.assertNotIn("upscaled", output)


if __name__ == "__main__":
    unittest.main()
