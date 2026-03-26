'''
Data models for subtitle offset operations.
'''

from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class Status(Enum):
    '''Status of subtitle offset operation.'''

    DRY_RUN = "Dry run"
    OFFSET = "Offset"
    ERROR_FILE = "Error: Cannot read file"
    ERROR_WRITE = "Error: Cannot write file"
    SKIPPED_NO_SRT = "Skipped: No SRT files"


@dataclass
class OffsetResult:
    '''Result of processing a single SRT file.'''

    file_path: Path
    output_path: Path
    offset_ms: int
    cues_modified: int
    status: Status
