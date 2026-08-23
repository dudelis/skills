# Hack the Platform Article Guide

Use this guide as a baseline. Before drafting, compare it with recent relevant articles because the live corpus is authoritative.

## Frontmatter

```yaml
---
title: 'Outcome-focused article title'
date: YYYY-MM-DD
tags: ['Power Platform', 'Relevant Product', 'Article Type']
draft: true
layout: PostBanner
images: ['/static/images/<article-slug>/banner.png']
summary: One concrete sentence explaining what the reader will learn or build.
---
```

- Use a quoted title when punctuation makes YAML parsing ambiguous.
- Keep tags specific and reuse capitalization found in recent articles.
- Use the intended publish date, not an invented historical date.
- Keep the summary factual, specific, and shorter than the opening paragraph.

## MDX Components

Import only components used in the article:

```mdx
import Youtube from 'components/Youtube'
import BlogImage from 'components/BlogImage'
```

Use the repository's existing component syntax. Typical media:

```mdx
<Youtube link="{YOUTUBE_URL}" />

<BlogImage
  src="/static/images/<article-slug>/<descriptive-name>.png"
  alt="Specific description of what the screenshot shows"
/>
```

## Recommended Shape

1. Open with the concrete problem and why the reader should care.
2. State what the solution enables or what the reader will build.
3. Add a video section only when a real URL exists or a placeholder is explicitly agreed.
4. Explain the use case, prerequisites, and architecture before detailed steps.
5. Organize implementation into outcome-named or numbered H2 sections.
6. Pair commands and code with the reason they are needed and the expected result.
7. Include troubleshooting for realistic failure modes found during implementation.
8. Close with a concise summary, primary resources, related posts, and the requested call to action.

Not every article needs every section. A short focused fix should stay short.

## Voice and Quality

- Write as a practitioner helping another practitioner.
- Prefer direct sentences and concrete outcomes over marketing language.
- Define uncommon terms on first use; do not explain basic terms to an expert audience.
- Preserve the user's actual opinions and experiences, but never fabricate them.
- Use bold text sparingly for key UI labels, warnings, and outcomes.
- Use horizontal rules only where recent articles use them to separate major phases.
- Use language identifiers on fenced code blocks whenever known.
- Make every screenshot alt text meaningful and every link descriptive.

## Final Checks

- Frontmatter parses and uses the current field order.
- The title, summary, introduction, and conclusion promise the same outcome.
- Commands, APIs, permissions, limits, and product names are verified.
- Secrets, tenant IDs, environment URLs, and personal data are removed or replaced.
- Imports are used; links and local asset paths resolve or are reported as missing.
- All placeholders are listed for the user.
- The article remains `draft: true` until publication is explicitly approved.
