'''
NFO file parsing utilities.
'''

import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Optional

from nforename.models import MediaType


def find_nfo_file(folder: Path) -> Optional[Path]:
    '''
    Find .nfo file in folder.

    Priority:
    1. movie.nfo
    2. tvshow.nfo
    3. Any other .nfo file
    '''
    primary_movie = folder / "movie.nfo"
    primary_tvshow = folder / "tvshow.nfo"

    if primary_movie.exists():
        return primary_movie
    if primary_tvshow.exists():
        return primary_tvshow

    for nfo in folder.glob("*.nfo"):
        if nfo.name not in ("movie.nfo", "tvshow.nfo"):
            return nfo

    return None


def detect_media_type(nfo_path: Path) -> Optional[MediaType]:
    '''Detect media type from .nfo root element.'''
    try:
        tree = ET.parse(nfo_path)
        root = tree.getroot()
        if root.tag == "movie":
            return MediaType.MOVIE
        if root.tag == "tvshow":
            return MediaType.SHOWS
    except ET.ParseError:
        pass
    return None


def extract_year(nfo_path: Path) -> Optional[str]:
    '''Extract year from .nfo file.'''
    try:
        tree = ET.parse(nfo_path)
        year_elem = tree.getroot().find("year")
        if year_elem is not None and year_elem.text:
            return year_elem.text.strip()
    except ET.ParseError:
        pass
    return None
