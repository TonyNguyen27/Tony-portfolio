#!/usr/bin/env python3
"""Fetch YouTube transcripts into research/youtube-transcripts/."""

from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "youtube-transcripts"

VIDEOS = {
    "jason-bay-cold-email-subject-lines": ("gLE5-_SDOCo", "Jason Bay", "[Tactics] Cold Email: Subject line formulas for 40-50%+ open rates"),
    "josh-braun-write-cold-email": ("lVUDHxrZJCY", "Josh Braun", "Let's Write a Good Cold Email"),
    "alex-berman-killer-cold-emails": ("881Dr4lMey4", "Alex Berman", "How To Write Killer Cold Emails That GUARANTEE Responses"),
    "morgan-ingram-linkedin-messaging": ("qktFZmgMJ3U", "Morgan J. Ingram", "How This LinkedIn Messaging Hack Made Me $120,000"),
    "kyle-coleman-scaling-outbound": ("Y7QLIHx1wpw", "Kyle Coleman", "Scaling Your Outbound Engine"),
    "will-allred-lavender-interview": ("5ZJFp7jkT-k", "Will Allred", "Interview with Will Allred, Co-Founder at Lavender.ai"),
    "patrick-dang-cold-email-tips": ("W-znS2Tkl8o", "Patrick Dang", "TOP 5 Cold Email Tips to DOMINATE B2B Sales"),
    "florin-tatulea-cold-email-secrets": ("aaFjjDBBEzk", "Florin Tatulea", "Cold Email Secrets from Outbound Expert Florin Tatulea"),
    "sam-mckenna-sales-email-workshop": ("whtxsPEBHEU", "Samantha McKenna", "#samsales Sales Email Writing Workshop"),
    "becc-holland-cold-email-teardown": ("Hgp3WEA494Y", "Becc Holland", "LIVE Cold email teardown with Becc Holland"),
}


def main() -> None:
    api = YouTubeTranscriptApi()
    OUT.mkdir(parents=True, exist_ok=True)

    for slug, (video_id, author, title) in VIDEOS.items():
        url = f"https://www.youtube.com/watch?v={video_id}"
        transcript = api.fetch(video_id)
        full = "\n".join(s.text for s in transcript)
        body = f"""# {author} - YouTube Transcript

Video Title: {title}

Video Link: {url}

Topic: B2B SaaS cold outreach pipeline

Date Collected: 2026-05-19

Source: youtube-transcript-api (auto-generated captions)

---

# Transcript

{full}

---

# Key Takeaways

(See research/other/frameworks-synthesis.md and sources.md.)
"""
        (OUT / f"{slug}.md").write_text(body)
        print(f"OK {slug} ({len(full)} chars)")


if __name__ == "__main__":
    main()
