# Media Utilitiy

A collection of command-line tools for managing and organizing my personal self-hosted media libraries.

## Installation

### Install Directly from GitHub

```bash
# Install nforename
pip install git+https://github.com/hdytrfli/media-utility.git#subdirectory=nforename

# Install extractsub
pip install git+https://github.com/hdytrfli/media-utility.git#subdirectory=extractsub

# Install offsetsub
pip install git+https://github.com/hdytrfli/media-utility.git#subdirectory=offsetsub
```

### Install from Local Clone

```bash
# Clone the repository
git clone https://github.com/hdytrfli/media-utility.git
cd media-utility

# Install individual tools
pip install -e ./nforename
pip install -e ./extractsub
pip install -e ./offsetsub
```

## Tools

### 1. NfoRename

Automatically rename movie and TV show folders by adding the year from `.nfo` files.

**Features:**
- Auto-detects media type (movies/shows) from `.nfo` files
- Safe dry-run mode to preview changes
- Smart skipping of folders that already have a year
- Clean tabular output with statistics

**Usage:**
```bash
# Dry-run (preview changes)
nforename ./movies

# Actually rename folders
nforename ./movies --execute

# Disable progress bar
nforename ./movies --no-progress
```

[Full documentation →](nforename/README.md)

---

### 2. ExtractSub

Extract embedded subtitles from MKV files and optionally remove them from the original file.

**Features:**
- Auto-detects all subtitle tracks in MKV files
- Safe dry-run mode to preview extraction
- Multiple codec support (SRT, ASS, PGS, VobSub, WebVTT)
- Extracts to current directory by default
- Automatic filename sanitization
- Optional removal of subtitles from original file

**Requirements:**
- [MKVToolNix](https://mkvtoolnix.download/) (mkvmerge/mkvextract)

**Usage:**
```bash
# Dry-run (preview extraction)
extractsub ./movies

# Actually extract subtitles
extractsub ./movies --execute

# Extract and remove from original file
extractsub ./movies --execute --remove

# Custom output directory
extractsub ./movies --execute --output ./subtitles
```

[Full documentation →](extractsub/README.md)

---

### 3. OffsetSub

Apply time offset to SRT subtitle files (sync subtitles).

**Features:**
- Accepts single file or directory
- Positive and negative offsets (milliseconds)
- Safe dry-run mode to preview changes
- Clean tabular output with statistics
- Custom output directory support

**Usage:**
```bash
# Dry-run (preview changes)
offsetsub ./subtitles --amount 500

# Delay subtitles by 500ms
offsetsub ./subtitles --amount 500 --execute

# Sync subtitles 1000ms earlier
offsetsub ./subtitles --amount -1000 --execute

# Process a single file
offsetsub ./movie.srt --amount 250 --execute

# Custom output directory
offsetsub ./subtitles --amount 500 --execute --output ./synced
```

[Full documentation →](offsetsub/README.md)

---

## Quick Start

### Typical Workflow

1. **Organize folder names** with `nforename`:
   ```bash
   nforename ./media --execute
   ```

2. **Extract subtitles** with `extractsub`:
   ```bash
   extractsub ./media --execute --remove
   ```

3. **Sync subtitles** if needed with `offsetsub`:
   ```bash
   offsetsub ./media/extracted --amount 500 --execute
   ```

---

## Requirements

- Python 3.10+
- MKVToolNix (for extractsub only)

## License

MIT License
