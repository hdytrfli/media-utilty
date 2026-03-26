'''
Command-line interface for offsetsub.
'''

import argparse
from pathlib import Path

from tabulate import tabulate

from offsetsub.models import Status
from offsetsub.srt_processor import process_path


def print_table(results) -> None:
    '''Print results in tabular format.'''
    if not results:
        print("No SRT files found")
        return

    table_data = []
    for r in sorted(results, key=lambda x: x.file_path.name):
        filename = r.file_path.name
        output = r.output_path.name if r.output_path else "-"
        cues = r.cues_modified
        status = r.status.value
        table_data.append([filename, output, cues, status])

    print()
    print(tabulate(table_data, headers=["FILE NAME", "OUTPUT", "CUES", "STATUS"], tablefmt="simple_grid"))
    print()
    print_statistics(results)


def print_statistics(results) -> None:
    '''Print summary statistics.'''
    stats = {
        "offset": sum(1 for r in results if r.status == Status.OFFSET),
        "dry_run": sum(1 for r in results if r.status == Status.DRY_RUN),
        "errors": sum(
            1
            for r in results
            if r.status in (Status.ERROR_FILE, Status.ERROR_WRITE)
        ),
    }

    print("Statistics:")
    print(f"  Offset:     {stats['offset']}")
    print(f"  Dry-run:    {stats['dry_run']}")
    print(f"  Errors:     {stats['errors']}")
    print(f"  Total:      {len(results)}")


def main():
    '''
    Main entry point.
    '''
    parser = argparse.ArgumentParser(
        description="Apply time offset to SRT subtitle files"
    )
    parser.add_argument(
        "path",
        type=Path,
        help="SRT file or directory containing SRT files"
    )
    parser.add_argument(
        "--amount",
        "-a",
        type=int,
        required=True,
        help="Offset amount in milliseconds (positive or negative)"
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Actually apply offset (default: dry-run)"
    )
    parser.add_argument(
        "--no-progress",
        action="store_true",
        help="Disable progress bar"
    )
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=None,
        help="Output directory for modified subtitles (default: same as input)"
    )

    args = parser.parse_args()

    try:
        results = process_path(
            args.path,
            args.amount,
            dry_run=not args.execute,
            show_progress=not args.no_progress,
            output_dir=args.output
        )
        print_table(results)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
