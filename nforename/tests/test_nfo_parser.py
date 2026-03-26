"""Tests for NFO parser module."""

import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest

from nforename.nfo_parser import detect_media_type, extract_year, find_nfo_file
from nforename.models import MediaType


def create_nfo_file(folder: Path, filename: str, content: str) -> Path:
    """Helper to create .nfo file with given content."""
    nfo_path = folder / filename
    nfo_path.write_text(content, encoding="utf-8")
    return nfo_path


MOVIE_XML = '<?xml version="1.0" encoding="utf-8"?>\n<movie><title>Test</title></movie>'
TVSHOW_XML = '<?xml version="1.0" encoding="utf-8"?>\n<tvshow><title>Test</title></tvshow>'


class TestFindNfoFile:
    """Tests for find_nfo_file function."""

    def test_finds_movie_nfo(self, tmp_path):
        """Should find movie.nfo when it exists."""
        create_nfo_file(tmp_path, "movie.nfo", MOVIE_XML)
        result = find_nfo_file(tmp_path)
        assert result == tmp_path / "movie.nfo"

    def test_finds_tvshow_nfo(self, tmp_path):
        """Should find tvshow.nfo when it exists."""
        create_nfo_file(tmp_path, "tvshow.nfo", TVSHOW_XML)
        result = find_nfo_file(tmp_path)
        assert result == tmp_path / "tvshow.nfo"

    def test_prefers_movie_nfo_over_other(self, tmp_path):
        """Should prefer movie.nfo over other .nfo files."""
        create_nfo_file(tmp_path, "movie.nfo", MOVIE_XML)
        create_nfo_file(tmp_path, "other.nfo", MOVIE_XML)
        result = find_nfo_file(tmp_path)
        assert result == tmp_path / "movie.nfo"

    def test_prefers_tvshow_nfo_over_other(self, tmp_path):
        """Should prefer tvshow.nfo over other .nfo files."""
        create_nfo_file(tmp_path, "tvshow.nfo", TVSHOW_XML)
        create_nfo_file(tmp_path, "other.nfo", TVSHOW_XML)
        result = find_nfo_file(tmp_path)
        assert result == tmp_path / "tvshow.nfo"

    def test_falls_back_to_any_nfo(self, tmp_path):
        """Should fall back to any .nfo file when no primary exists."""
        create_nfo_file(tmp_path, "random.nfo", MOVIE_XML)
        result = find_nfo_file(tmp_path)
        assert result == tmp_path / "random.nfo"

    def test_returns_none_when_no_nfo(self, tmp_path):
        """Should return None when no .nfo file exists."""
        result = find_nfo_file(tmp_path)
        assert result is None


class TestDetectMediaType:
    """Tests for detect_media_type function."""

    def test_detects_movie(self, tmp_path):
        """Should detect movie type."""
        nfo_path = create_nfo_file(tmp_path, "test.nfo", MOVIE_XML)
        result = detect_media_type(nfo_path)
        assert result == MediaType.MOVIE

    def test_detects_shows(self, tmp_path):
        """Should detect shows type."""
        nfo_path = create_nfo_file(tmp_path, "test.nfo", TVSHOW_XML)
        result = detect_media_type(nfo_path)
        assert result == MediaType.SHOWS

    def test_returns_none_for_invalid_xml(self, tmp_path):
        """Should return None for invalid XML."""
        nfo_path = create_nfo_file(tmp_path, "test.nfo", "not xml")
        result = detect_media_type(nfo_path)
        assert result is None

    def test_returns_none_for_unknown_root(self, tmp_path):
        """Should return None for unknown root element."""
        nfo_path = create_nfo_file(tmp_path, "test.nfo", '<?xml version="1.0"?><unknown></unknown>')
        result = detect_media_type(nfo_path)
        assert result is None


class TestExtractYear:
    """Tests for extract_year function."""

    def test_extracts_year(self, tmp_path):
        """Should extract year from .nfo file."""
        nfo_path = create_nfo_file(
            tmp_path, "test.nfo", '<?xml version="1.0" encoding="utf-8"?><movie><year>2023</year></movie>'
        )
        result = extract_year(nfo_path)
        assert result == "2023"

    def test_strips_year_whitespace(self, tmp_path):
        """Should strip whitespace from year."""
        nfo_path = create_nfo_file(
            tmp_path, "test.nfo", '<?xml version="1.0" encoding="utf-8"?><movie><year>  2023  </year></movie>'
        )
        result = extract_year(nfo_path)
        assert result == "2023"

    def test_returns_none_when_no_year(self, tmp_path):
        """Should return None when no year tag exists."""
        nfo_path = create_nfo_file(tmp_path, "test.nfo", MOVIE_XML)
        result = extract_year(nfo_path)
        assert result is None

    def test_returns_none_when_year_empty(self, tmp_path):
        """Should return None when year tag is empty."""
        nfo_path = create_nfo_file(
            tmp_path, "test.nfo", '<?xml version="1.0" encoding="utf-8"?><movie><year></year></movie>'
        )
        result = extract_year(nfo_path)
        assert result is None

    def test_returns_none_for_invalid_xml(self, tmp_path):
        """Should return None for invalid XML."""
        nfo_path = create_nfo_file(tmp_path, "test.nfo", "not xml")
        result = extract_year(nfo_path)
        assert result is None
