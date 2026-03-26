# OffsetSub

Apply time offset to SRT subtitle files.

## Installation

### Install from GitHub

```bash
pip install git+https://github.com/hdytrfli/media-utilty.git#subdirectory=offsetsub
```

### Install from Local Clone

```bash
git clone https://github.com/hdytrfli/media-utilty.git
cd media-utilty/offsetsub
pip install -e .
```

## Features

- **Accepts file or directory** - Process a single SRT file or all SRT files in a directory
- **Positive and negative offsets** - Delay subtitles (positive) or sync earlier (negative)
- **Safe dry-run mode** - Preview changes before applying
- **Clean tabular output** - Easy to read results with statistics
- **Custom output directory** - Specify where to save modified subtitles

## Usage

```bash
# Dry-run (default) - shows what would be changed
offsetsub ./subtitles --amount 500

# Actually apply offset (delay subtitles by 500ms)
offsetsub ./subtitles --amount 500 --execute

# Sync subtitles earlier by 1000ms
offsetsub ./subtitles --amount -1000 --execute

# Process a single file
offsetsub ./movie.srt --amount 250 --execute

# Specify output directory
offsetsub ./subtitles --amount 500 --execute --output ./synced

# Disable progress bar
offsetsub ./subtitles --amount 500 --no-progress
```

## Examples

**Delay subtitles by 500ms:**

```bash
offsetsub ./subtitles --amount 500 --execute
```

**Sync subtitles 2 seconds earlier:**

```bash
offsetsub ./subtitles --amount -2000 --execute
```

**Process a single file:**

```bash
offsetsub ./movie.srt --amount 150 --execute
```

## Sample Output

```
┌──────────────────────────────┬──────────────────────────────┬────────┬───────────────────┐
│ FILE NAME                    │ OUTPUT                       │   CUES │ STATUS            │
├──────────────────────────────┼──────────────────────────────┼────────┼───────────────────┤
│ movie.srt                    │ subtitles                    │    807 │ Offset            │
├──────────────────────────────┼──────────────────────────────┼────────┼───────────────────┤
│ show_s01e01.srt              │ subtitles                    │    523 │ Offset            │
└──────────────────────────────┴──────────────────────────────┴────────┴───────────────────┘

Statistics:
  Offset:     2
  Dry-run:    0
  Errors:     0
  Total:      2
```

## How It Works

1. Scans the target path for `.srt` files (file or directory)
2. Parses each subtitle cue's timestamps
3. Applies the offset in milliseconds to start and end times
4. Ensures timestamps don't go negative (clamped to 00:00:00,000)
5. Writes modified subtitles to output directory

## Offset Values

- **Positive values** - Delay subtitles (make them appear later)
- **Negative values** - Sync subtitles earlier (make them appear sooner)

### Common Use Cases

| Issue | Solution |
|-------|----------|
| Subtitles appear too early | Use negative offset (e.g., `-500`) |
| Subtitles appear too late | Use positive offset (e.g., `500`) |
| Audio/video desync | Adjust offset until synced |

## License

MIT License
