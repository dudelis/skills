---
name: write-blog-article
description: Plans, researches, drafts, and revises technical MDX articles and their banner artwork in the established Hack the Platform style. Use when the user wants to write, outline, generate, illustrate, or improve an article for hacktheplatform.dev or the pp-blog repository.
argument-hint: "Article topic, rough idea, or source material"
---

# Write a Hack the Platform Article

Create practical technical articles for the blog repository. Treat `C:\_dev\pp-blog` as the default repository and `data/blog` as the article directory. If either path is unavailable, ask for the correct location.

## Start With Local Context

1. Read at least three recent, relevant published `.mdx` articles from `data/blog`.
2. Prefer recent posts over old starter-template drafts when inferring style.
3. Inspect any related source code, images, video, or notes supplied by the user.
4. Use [ARTICLE-GUIDE.md](ARTICLE-GUIDE.md) for the baseline structure, then follow stronger conventions found in the current repository.

Do not ask the user for information that can be discovered from these sources.

## Interview

Ask one question at a time and wait for the answer. Include a recommended answer or a short set of options when useful. Cover only unresolved items:

1. What should the reader be able to do or understand afterward?
2. Who is the reader, and what can they already be expected to know?
3. Is this a tutorial, explanation, troubleshooting guide, announcement, or series entry?
4. What source material exists: code, repository, notes, screenshots, demo environment, or video URL?
5. What constraints, caveats, versions, or failed approaches must be covered?
6. What publish date, tags, series links, and closing call to action are wanted?
7. Should the article include one banner direction or three distinct options to choose from?

If the initial request already answers several questions, skip them. Stop interviewing once the article can be outlined without guessing about its purpose or evidence.

## Agree on the Outline

Present a compact outline containing:

- working title and one-sentence promise
- intended audience and prerequisites
- ordered sections and the purpose of each
- required code, screenshots, diagrams, and links
- facts that still need verification
- banner count and visual constraints

Ask for approval before drafting. Incorporate feedback into the outline rather than starting a second competing outline.

## Research and Verify

- Prefer official Microsoft or primary documentation for technical claims.
- Check current commands, limits, permissions, product names, and prerequisites.
- Validate code and commands locally when the repository provides a practical check.
- Never invent test results, screenshots, URLs, product behavior, or personal experience.
- Mark unresolved values with explicit placeholders such as `{YOUTUBE_URL}` or `TODO: screenshot`, and list them after the draft.

## Design the Banner

Follow [BANNER-GUIDE.md](BANNER-GUIDE.md) after the article promise and outline are stable.

1. Derive one shared communication goal from the article's central problem and outcome.
2. Unless the user requests one banner, propose three concept briefs with genuinely different settings, compositions, metaphors, media, and moods. A palette swap does not count as a different concept.
3. Show the concept briefs and recommend one. Ask for approval before spending generation calls.
4. If an image-generation tool is available, generate the approved options at `1536x1024` and save them beside the article assets as `banner-option-1.png`, `banner-option-2.png`, and `banner-option-3.png`.
5. Show every generated option to the user. After selection, save the chosen image as `banner.png` and update frontmatter. Do not overwrite an existing banner without confirmation.
6. If no image-generation tool is available, write production-ready prompts for the approved concepts and clearly state that no image files were created.

## Draft the Article

1. Create `data/blog/<descriptive-kebab-case-slug>.mdx` unless the user chooses another path.
2. Use the repository's current frontmatter order and `layout: PostBanner` convention.
3. Set `draft: true` until the user explicitly approves publication readiness.
4. Add only MDX component imports actually used by the article.
5. Write in the first person where it reflects user-provided experience; otherwise use direct, evidence-based language.
6. Keep the article task-oriented: explain why each major step matters, provide copyable examples, and cover likely failure modes.
7. Link claims and prerequisites to primary sources. Use existing repository conventions for screenshots, video, and related posts.
8. Create banner files only through the approved banner workflow. For other images, reference agreed paths and clearly report missing assets.

## Review

After writing, check the file for valid frontmatter, coherent heading order, fenced-code languages, working local links, used imports, banner dimensions, missing assets, placeholders, and consistency with recent posts. Run repository lint, format, or build checks when available.

Present the draft path, the article's structure, verification performed, and any remaining placeholders. Ask whether anything is missing or unclear and whether any section should be more or less detailed. Revise the same file from the user's feedback.
