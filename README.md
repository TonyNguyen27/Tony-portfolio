# Cursor IDE Setup

## Tools I Installed
- Cursor IDE
- Claude Code extension
- Codex extension

## Steps I Completed
1. Downloaded and installed Cursor IDE from cursor.com
2. Installed Claude Code extension and logged in
3. Installed Codex extension and logged in
4. Created a public GitHub repository
5. Opened the repository in Cursor
6. Created and edited this README.md
7. Committed and pushed the README to GitHub.

## Issues I Ran Into
Earlier this year, I started exploring vibe coding and built a few tools on my own through trial and error. I'm still far from being a strong coder, but I show up and learn something new every day. That's why Cursor was already part of my setup from the start. 

So far I've used it to vibe code a few tools: building marketing strategy plans, researching industries, and generating budget allocations straight from a client brief.

But when I run into code-related issues, I handle them in two ways:
- First, I screenshot the error or the step I'm stuck on and ask AI to help me work through it.
- Second, if the issue persists, I reach out to friends who have a coding background. Part of it is that I genuinely enjoy working on tech projects, so naturally I've built a circle of developer friends over time. I'll ask them to walk me through it, and honestly, it gets resolved pretty quickly, usually in ways I never would have thought of on my own.

## Research: Cold Outreach for B2B SaaS

I collected recent content from **10 practitioners** who run or scale outbound (not commentators only). Topic: building a cold outreach pipeline for B2B SaaS (email, LinkedIn, calls).

**Why these experts:** Each has done the work—SDR/AE, founder GTM, or trains teams on live campaigns (Jason Bay, Josh Braun, Alex Berman, Morgan J. Ingram, Kyle Coleman, Will Allred, Patrick Dang, Florin Tatulea, Samantha McKenna, Becc Holland).

**What’s in the repo:**

| Path | Contents |
|------|----------|
| [`research/sources.md`](research/sources.md) | Expert list, links, dates, annotations |
| [`research/linkedin-posts/`](research/linkedin-posts/) | 2 posts per author (public URLs, summaries) |
| [`research/youtube-transcripts/`](research/youtube-transcripts/) | 10 videos — fetched via `youtube-transcript-api` |
| [`research/other/`](research/other/) | Collection methods + cross-expert synthesis |
| [`scripts/fetch_youtube_transcripts.py`](scripts/fetch_youtube_transcripts.py) | Re-run transcript pulls |

**Tools used:** Cursor + Claude Code; Python `youtube-transcript-api` for YouTube; manual collection for LinkedIn public posts.