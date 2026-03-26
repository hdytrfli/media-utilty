'''
Data models for media rename operations.
'''

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Optional


class MediaType(Enum):
    '''Type of media content.'''

    MOVIE = "movie"
    SHOWS = "shows"


class Status(Enum):
    '''Status of folder processing.'''

    DRY_RUN = "Dry run"
    ERROR_CONFLICT = "Error: Conflict"
    ERROR_RENAME = "Error: Rename"
    RENAMED = "Renamed"
    SKIPPED_HAS_YEAR = "Skipped: Has year"
    SKIPPED_NO_NFO = "Skipped: No .nfo"
    SKIPPED_NO_YEAR = "Skipped: No year"
    SKIPPED_WRONG_TYPE = "Skipped: Wrong type"


@dataclass
class RenameResult:
    '''Result of processing a single folder.'''

    old_path: Path
    new_path: Optional[Path]
    year: Optional[str]
    media_type: Optional[MediaType]
    status: Status
