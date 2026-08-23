---
name: write-youtube-video
description: Turns a technical article or problem description into a step-by-step YouTube recording plan, spoken script, upload metadata, and thumbnail concept. Use when the user wants to plan, script, record, title, package, or publish a tutorial, demo, troubleshooting video, or technical explanation for YouTube.
argument-hint: "Article path, draft, problem description, or video idea"
---

# Write a YouTube Video

Create a recording-ready package for a practical YouTube video. Use an article as source material when one exists; otherwise develop the video from the user's description.

## Establish the Source

1. If the user provides an article, file, URL, notes, code, or demo environment, inspect it before asking questions.
2. If no article is available, accept a rough problem or explanation as the starting point.
3. Treat supplied material as evidence, not automatically as current fact. Flag unsupported claims and placeholders.
4. Do not ask for information that can be discovered from the source or current workspace.

## Interview

Ask one question at a time and wait for the answer. Offer a recommended answer or a few useful options when possible. Cover only unresolved items:

1. What should the viewer understand or be able to do afterward?
2. Who is the viewer, and what knowledge can be assumed?
3. Is this a live demo, tutorial, explanation, troubleshooting video, or another format?
4. What target length, language, tone, and presenter style are wanted?
5. What exact problem, approach, steps, result, and caveats must be shown?
6. What code, environment, accounts, screenshots, diagrams, or B-roll are available?
7. What must be hidden, mocked, pre-recorded, or replaced to protect secrets and personal data?
8. What call to action, links, playlist, and upload defaults should be used?

Stop when the structure and evidence can be planned without guessing. Never invent personal experience, product behavior, or demo results.

## Agree on the Recording Plan

Present a compact plan with:

- working title and one-sentence viewer promise
- format, audience, prerequisites, and target duration
- ordered segments with time budgets and purpose
- demo setup, assets, shots, transitions, and backup captures
- claims or product details that still require verification

Ask for approval before writing the full script. Revise this plan rather than producing competing plans.

## Verify and Prepare

- Prefer primary or official sources for technical claims.
- Check current commands, UI names, prerequisites, permissions, and platform upload limits.
- Validate commands or code locally when a practical check exists.
- Replace secrets, tenant details, personal data, and unstable identifiers with safe demo values.
- Mark unresolved items with explicit placeholders such as `{DEMO_URL}` or `TODO: capture success screen`.

## Create the Video Package

Create `videos/<descriptive-kebab-case-slug>/VIDEO-PACKAGE.md` in the current workspace unless the user chooses another location. Follow [VIDEO-PACKAGE-GUIDE.md](VIDEO-PACKAGE-GUIDE.md).

The package must contain:

1. The approved recording plan and setup checklist.
2. A step-by-step script with timestamps, natural spoken narration, on-screen actions, expected results, and edit notes.
3. One recommended YouTube title plus useful alternatives.
4. Upload-ready description, chapters, tags, hashtags, settings, pinned comment, and placeholders for links.
5. A thumbnail concept, short thumbnail copy, composition, and reproducible image-generation prompt.

When image-generation or image-editing tools are available, create `thumbnail.png` at 1280x720 from the approved concept. Use supplied real assets where appropriate. Always retain the thumbnail brief and prompt in `VIDEO-PACKAGE.md`; never claim an image was created when it was not.

## Review

Check that timings approximately match the target length, every demo action has narration and a success cue, chapters match the final segments, metadata promises the same outcome as the script, and all placeholders and missing assets are listed. Report the package path, thumbnail path or limitation, verification performed, and unresolved items.

Ask whether the script sounds natural in the user's voice, whether anything is missing or unclear, and whether any section should be more or less detailed. Revise the same package from feedback.