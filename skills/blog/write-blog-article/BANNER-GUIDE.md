# Hack the Platform Banner Guide

Create banner artwork that communicates the article's technical idea at a glance. The image should complement the title, not render the title inside the artwork.

## Output Contract

- Default canvas: `1536x1024` pixels, 3:2 landscape.
- Candidate files: `public/static/images/<article-slug>/banner-option-1.png` through `banner-option-3.png`.
- Selected file: `public/static/images/<article-slug>/banner.png`.
- Frontmatter path: `/static/images/<article-slug>/banner.png`.
- Keep the main subject inside the central 70% so responsive crops do not remove it.
- Prefer PNG unless the repository's current convention for comparable artwork differs.
- Do not overwrite or delete existing artwork without explicit approval.

## Three-Direction Rule

Each option must express the same article topic through a different visual thesis. Change at least three of these axes between every pair:

1. **Setting**: abstract data space, physical workspace, architectural environment, workshop, control room, or another topic-relevant world.
2. **Composition**: single focal object, left-to-right process, layered system map, before/after contrast, or human-scale scene.
3. **Metaphor**: bridge, gateway, assembly line, lock and key, signal path, translation, orchestration, or a metaphor derived from the article.
4. **Medium**: clean vector editorial, tactile paper cut, isometric 3D, cinematic realism, technical blueprint, or another deliberate treatment.
5. **Palette and mood**: choose colors and lighting that support the concept rather than recoloring the same scene.
6. **Perspective**: orthographic, top-down, close-up, wide environmental, or diagrammatic.

Do not submit three near-identical layouts, the same objects rearranged slightly, or one prompt with different colors.

## Concept Brief

Before generation, describe each option with:

```text
Name:
Visual thesis:
Setting and focal subject:
Composition and perspective:
Medium, palette, and mood:
Topic details that must be recognizable:
What this option deliberately avoids:
```

Recommend the concept that communicates the article outcome most clearly, but let the user approve one, two, or all three for generation.

## Prompt Requirements

Every generation prompt must specify:

- the article's technical topic and intended visual message
- the approved setting, metaphor, composition, perspective, medium, and palette
- a landscape 3:2 composition with a crop-safe central subject
- no title, captions, random letters, watermarks, signatures, or fake UI text
- no unsupported product logos or inaccurate brand marks
- only the minimum recognizable technical objects needed to explain the idea
- clean separation between major elements and enough negative space for responsive display

Write each prompt independently. Do not reuse a shared base prompt whose only variables are style or color.

## Review Generated Options

Inspect each actual file, not only the prompt. Reject and regenerate an option when it:

- misrepresents the article's technical relationship
- contains illegible text, malformed symbols, or misleading UI
- is visually too similar to another option
- places critical content near an edge
- looks like generic technology decoration without a clear topic signal

After the user selects an option, make it `banner.png`. Keep unselected candidates until the user asks to remove them.
