# Collection Methods

## YouTube transcripts

- **Tool:** [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) (Python 1.2.x)
- **API usage:** `YouTubeTranscriptApi().fetch(video_id)` — pulls auto-generated or manual captions when available
- **No API key required** (unlike Supadata paid tier)
- **Limitations:** Caption quality varies; some videos lack English captions; very long workshops produce large markdown files

## LinkedIn posts

- **Folder:** `research/linkedin-posts/` — **LinkedIn only.** Do not put YouTube, Substack, podcast, or course links here; those belong in `sources.md`, `youtube-transcripts/`, or `other/`.
- **Method:** Manual collection from public LinkedIn post URLs (guest-visible text)
- **Not used:** Authenticated scraping APIs (ToS risk; no credentials in repo)
- **Fields captured:** URL, approximate date, topic, summary, key insights

## Dates

- LinkedIn shows relative times ("1y", "4mo"); recorded as approximate in each post file
- Transcript pull date: **2026-05-19**
