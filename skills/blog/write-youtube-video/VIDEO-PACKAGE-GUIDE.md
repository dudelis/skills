# YouTube Video Package Guide

Use this contract for `VIDEO-PACKAGE.md`. Adapt the depth to the video; do not pad a focused explanation to fill every section.

## 1. Video Brief

- **Recommended title:** One clear, accurate title that leads with the viewer outcome.
- **Alternative titles:** Two or three meaningfully different options, not punctuation variants.
- **Viewer promise:** One sentence describing what the viewer will understand or achieve.
- **Audience and prerequisites:** Expected role, knowledge, tools, and access.
- **Format and target length:** Demo, tutorial, explanation, troubleshooting, or hybrid.
- **Source material:** Article, code, documentation, notes, and assets used.

## 2. Recording Plan

Use a table with these columns:

| Time | Segment | Purpose | Visual / action | Asset or setup |
| ---- | ------- | ------- | --------------- | -------------- |

Include:

- a hook that immediately names or demonstrates the real problem
- enough context to make the solution understandable
- setup and prerequisites before dependent steps
- the main explanation or demo in causal order
- a visible success result and realistic caveats
- a concise recap and requested call to action

List pre-recording setup separately: accounts, sample data, browser tabs, terminal state, code branch, zoom level, notifications, secret removal, screen resolution, microphone, and backup screenshots or clips.

## 3. Step-by-Step Script

Create one subsection per segment:

```md
### 02:10-03:25 - Configure the connection

**Goal:** Explain why this setting is required.

**Say:**
Natural spoken wording for the presenter. Keep sentences easy to say aloud.

**Show:**
1. Open **Settings**.
2. Select the connection.
3. Confirm that the status changes to **Connected**.

**Success cue:** The exact result the viewer should see.

**Edit notes:** Zoom, callout, cut, B-roll, correction overlay, or backup capture.
```

- Separate narration from stage direction; never make the presenter read UI instructions verbatim.
- Explain why before or while showing how.
- Include exact commands and code blocks when the viewer needs to copy them.
- Add pronunciation notes only for terms likely to interrupt delivery.
- Use `TODO` placeholders for missing captures or unverified behavior.
- Keep timestamps internally consistent and revise them after script changes.

## 4. YouTube Metadata

Provide upload-ready content:

- **Title:** The recommended title, checked against YouTube's current title limit.
- **Description:** Start with two concrete lines that stand alone before expansion. Follow with a short summary, prerequisites, resources, chapters, disclosure or attribution when needed, and the call to action.
- **Chapters:** Derive from final timestamps; start at `00:00` and use descriptive labels.
- **Tags:** Focused topic, product, problem, and audience terms; avoid irrelevant keyword stuffing.
- **Hashtags:** Up to three highly relevant choices, kept separate from tags.
- **Pinned comment:** A useful question, key link, correction note, or next step.

Recommend values for each relevant upload setting and explain non-obvious choices:

- category, video language, title/description language, and caption status
- audience designation, paid promotion, and altered or synthetic content disclosure
- visibility or schedule, playlist, license, embedding, comments, and moderation
- recording date/location only when useful and safe
- end screen, cards, related video, subtitles, and thumbnail

Do not guess legal, disclosure, audience, or sponsorship answers. Ask the user or leave a clearly labeled decision placeholder. Verify current platform limits rather than preserving numeric limits in the skill.

## 5. Thumbnail Brief

Include all of the following even when `thumbnail.png` is generated:

- **Concept:** The single visual idea and how it supports the title without repeating it.
- **Copy:** Prefer zero to four short words that remain readable on a small screen.
- **Composition:** Main subject, product or interface, background, hierarchy, contrast, and safe margins.
- **Asset list:** Supplied logos, screenshots, presenter photo, or product visuals and their source.
- **Generation prompt:** A reproducible prompt specifying 16:9 composition, 1280x720 output, exact text, visual hierarchy, and exclusions.
- **Accessibility check:** Strong contrast, uncluttered focal point, and no meaning conveyed by color alone.

Use an honest, specific visual from the actual topic. Do not fabricate product UI or misleading before/after results. Avoid tiny interface text, generic stock imagery, excessive logos, and decorative clutter.

## 6. Final Checklist

- [ ] The title, hook, script, thumbnail, and description promise the same outcome.
- [ ] Segment timings approximately equal the target duration.
- [ ] Every action has an expected result or success cue.
- [ ] Commands, claims, product names, and prerequisites were verified or marked.
- [ ] Secrets, personal data, account details, and notifications are removed.
- [ ] Chapters match the final script timestamps.
- [ ] Links, assets, disclosures, and `TODO` placeholders are listed.
- [ ] The thumbnail file exists, or the package clearly says why only the brief was produced.