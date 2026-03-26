'''
Data models for subtitle extraction operations.
'''

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import List, Optional


class Status(Enum):
    '''Status of subtitle extraction operation.'''

    DRY_RUN = "Dry run"
    EXTRACTED = "Extracted"
    ERROR_NO_MKV = "Error: No MKV file"
    ERROR_NO_SUBS = "Error: No subtitles"
    ERROR_PROBE = "Error: Cannot probe file"
    ERROR_EXTRACT = "Error: Extraction failed"
    SKIPPED_NO_SUBS = "Skipped: No embedded subtitles"


@dataclass
class SubtitleTrack:
    '''Information about a subtitle track.'''

    track_id: int
    language: Optional[str]
    codec: Optional[str]
    title: Optional[str]
    is_forced: bool
    is_default: bool


@dataclass
class ExtractResult:
    '''Result of processing a single MKV file.'''

    file_path: Path
    output_path: Optional[Path]
    subtitle_tracks: List[SubtitleTrack]
    status: Status
