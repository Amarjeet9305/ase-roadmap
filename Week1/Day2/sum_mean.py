#!/usr/bin/env python3
"""
sum_mean.py - CLI utility to compute sum and mean of numbers.

Usage examples:
  python sum_mean.py --numbers "1 2 3 4"
  python sum_mean.py -n "1,2,3,4"
  python sum_mean.py --file numbers.txt
  python sum_mean.py --interactive
  python sum_mean.py            # prompts interactively if no flag provided
"""

import argparse
import sys
import re
from typing import List

def parse_numbers_from_string(s: str) -> List[float]:
    """
    Parse a string containing numbers separated by commas/spaces/semicolons/newlines
    into a list of floats. Raises ValueError if any token is not a number.
    """
    if s is None:
        return []
    # split on commas, whitespace, semicolons
    tokens = re.split(r'[,\s;]+', s.strip())
    nums: List[float] = []
    for t in tokens:
        if t == '':
            continue
        try:
            nums.append(float(t))
        except ValueError as e:
            raise ValueError(f"Cannot parse token '{t}' as a number.") from e
    return nums

def read_numbers_from_file(path: str) -> List[float]:
    """Read file contents and parse numbers from it."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except OSError as e:
        raise OSError(f"Error reading file '{path}': {e.strerror}") from e
    return parse_numbers_from_string(content)

def compute_sum(nums: List[float]) -> float:
    """Return the sum of numbers."""
    return sum(nums)

def compute_mean(nums: List[float]) -> float:
    """Return the mean (average) of numbers. Raises ZeroDivisionError for empty list."""
    if len(nums) == 0:
        raise ZeroDivisionError("Cannot compute mean of empty list.")
    return sum(nums) / len(nums)

def main():
    parser = argparse.ArgumentParser(
        description="Compute sum and mean of a list of numbers (from CLI, file or interactive input)."
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-n', '--numbers', type=str,
                       help='Numbers as comma/space separated string. e.g. "1 2 3" or "1,2,3"')
    group.add_argument('-f', '--file', type=str,
                       help='Path to file containing numbers separated by whitespace or commas.')
    group.add_argument('-i', '--interactive', action='store_true',
                       help='Prompt interactively for numbers (default if none supplied).')
    parser.add_argument('-p', '--precision', type=int, default=4,
                        help='Decimal places for mean (default: 4)')
    args = parser.parse_args()

    try:
        # Decide input source
        if args.numbers:
            nums = parse_numbers_from_string(args.numbers)
        elif args.file:
            nums = read_numbers_from_file(args.file)
        else:
            # default to interactive input if neither --numbers nor --file is given
            prompt = input("Enter numbers separated by space or comma (e.g. 1 2 3 or 1,2,3): ")
            nums = parse_numbers_from_string(prompt)

        if not nums:
            print("No numbers provided. Exiting.", file=sys.stderr)
            sys.exit(1)

        total = compute_sum(nums)
        mean = compute_mean(nums)

        print(f"Count : {len(nums)}")
        print(f"Sum   : {total}")
        print(f"Mean  : {mean:.{args.precision}f}")

    except Exception as e:
        # Print human-friendly error messages to stderr and exit with non-zero status
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
