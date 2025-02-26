#!/usr/bin/env python3

import os
import re
import argparse


def rename_files(new_prefix, target_path):
    """Renames files by replacing a two-digit prefix (00-99) with a custom text string."""
    if not os.path.exists(target_path):
        print(f"Error: Path '{target_path}' does not exist.")
        return
    # Ensure new prefix ends with " - "
    if not new_prefix.endswith(" - "):
        new_prefix += " - "
    # Get list of files in directory or handle single file
    files = [os.path.join(target_path, f) for f in os.listdir(target_path)] if os.path.isdir(target_path) else [target_path]
    # Regex pattern to match filenames starting with "00 - " to "99 - "
    pattern = re.compile(r"^(\d{2}) - (.+)$")
    for file_path in files:
        dir_name, filename = os.path.split(file_path)
        match = pattern.match(filename)
        if match:
            new_name = f"{new_prefix}{match.group(2)}"  # Keep everything after "XX - "
            new_path = os.path.join(dir_name, new_name)
            # Rename the file
            os.rename(file_path, new_path)
            print(f"Renamed: '{filename}' → '{new_name}'")


def main():
    parser = argparse.ArgumentParser(description="Rename files by replacing a two-digit prefix (00-99) with a custom prefix.")
    parser.add_argument("new_prefix", type=str, help="The text to replace the numeric prefix with (automatically adds ' - ' if missing).")
    parser.add_argument("target_path", type=str, help="The file or directory path containing files to rename.")
    args = parser.parse_args()
    rename_files(args.new_prefix, args.target_path)


if __name__ == "__main__":
    main()
