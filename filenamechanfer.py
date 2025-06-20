import os
import re

# Regex pattern to match 'Friends SXXEZZ'
pattern = re.compile(r'(Friends S\d{2}E\d{2})')

# Iterate through all files in the current directory
for filename in os.listdir('.'):
    if filename.lower().endswith(('.mp4', '.m4v', '.mkv')):
        match = pattern.search(filename)
        if match:
            new_filename = f"{match.group(1)}.mp4"
            if filename != new_filename:
                os.rename(filename, new_filename)
                print(f"Renamed: {filename} -> {new_filename}")
