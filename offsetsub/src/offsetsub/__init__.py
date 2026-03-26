'''
OffsetSub - Apply time offset to SRT subtitle files.
'''

from offsetsub.models import Status, OffsetResult
from offsetsub.srt_processor import (
    find_srt_files,
    parse_timestamp,
    format_timestamp,
    offset_srt_content,
    process_srt_file,
    process_path,
)
from offsetsub.cli import main

__version__ = "1.0.0"
__all__ = [
    "Status",
    "OffsetResult",
    "find_srt_files",
    "parse_timestamp",
    "format_timestamp",
    "offset_srt_content",
    "process_srt_file",
    "process_path",
    "main",
]
