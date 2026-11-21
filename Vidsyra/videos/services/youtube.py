import re
from urllib.parse import parse_qs, urlsplit

from django.core.exceptions import ValidationError


_YOUTUBE_HOSTS = {
    "youtube.com",
    "www.youtube.com",
    "m.youtube.com",
    "music.youtube.com",
    "youtu.be",
    "www.youtu.be",
    "youtube-nocookie.com",
    "www.youtube-nocookie.com",
}
_VIDEO_ID_PATTERN = re.compile(r"^[A-Za-z0-9_-]{11}$")


def extract_youtube_video_id(value: str) -> str:
    """Return the 11-character video ID from a supported YouTube URL.

    This function only parses the URL. It does not fetch video data or download
    media. Raise Django ValidationError for unsupported or malformed URLs.
    """
    if not isinstance(value, str) or not value.strip():
        raise ValidationError("Enter a YouTube video URL.")

    candidate = value.strip()
    if "://" not in candidate:
        candidate = f"https://{candidate}"

    try:
        parsed = urlsplit(candidate)
    except ValueError as exc:
        raise ValidationError("Enter a valid YouTube URL.") from exc

    if parsed.scheme not in {"http", "https"}:
        raise ValidationError("Only HTTP or HTTPS YouTube URLs are supported.")

    host = (parsed.hostname or "").lower()
    if host not in _YOUTUBE_HOSTS:
        raise ValidationError("The URL must belong to YouTube.")

    video_id = ""
    path_parts = [part for part in parsed.path.split("/") if part]

    if host in {"youtu.be", "www.youtu.be"}:
        video_id = path_parts[0] if path_parts else ""
    elif parsed.path.rstrip("/") == "/watch":
        video_id = parse_qs(parsed.query).get("v", [""])[0]
    elif len(path_parts) >= 2 and path_parts[0] in {"embed", "shorts", "live", "v"}:
        video_id = path_parts[1]

    if not _VIDEO_ID_PATTERN.fullmatch(video_id):
        raise ValidationError("Could not find a valid YouTube video ID in that URL.")

    return video_id
