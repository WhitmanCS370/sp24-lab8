import os
import csv
import json
import shutil
import sys
import time
from pathlib import Path

from hash_all import hash_all

# [file_name]
def fileName(backup_dir):
    for file_name in os.listdir(backup_dir):
        if (file_name.endswith(".csv") or file_name.endswith(".json")) and len(file_name) == 8 and file_name.isdigit(): #condition check for manifest file
            file_number = int(file_name.split(".")[0]) # split off the extension and convert to int
            file_number += 1
            return f"{file_number:08d}"
# [backup]
def backup(source_dir, backup_dir, file_type):
    manifest = hash_all(source_dir)
    timestamp = current_time()
    file_name = fileName(backup_dir)
    write_manifest(backup_dir, file_name, manifest, file_type)
    copy_files(source_dir, backup_dir, manifest)
    return manifest
# [/backup]

# [copy]
def copy_files(source_dir, backup_dir, manifest):
    for (filename, hash_code) in manifest:
        source_path = Path(source_dir, filename)
        backup_path = Path(backup_dir, f"{hash_code}.bck")
        if not backup_path.exists():
            shutil.copy(source_path, backup_path)
# [/copy]

# [time]
def current_time():
    return f"{time.time()}".split(".")[0]
# [/time]

# [write]
def write_manifest(backup_dir, file_name, manifest, file_type):
    backup_dir = Path(backup_dir)
    if file_type == 'csv' or file_type is None:
        extension = 'csv'
    elif file_type == 'json':
        extension = 'json'
    else:
        raise ValueError(f"File type needs to be csv or json")
    if not backup_dir.exists():
        backup_dir.mkdir()
    manifest_file = Path(backup_dir, f"{file_name}.{extension}")
    with open(manifest_file, "w") as raw:
        writer = csv.writer(raw)
        writer.writerow(["filename", "hash"])
        writer.writerows(manifest)
# [/write]

if __name__ == "__main__":
    assert len(sys.argv) == 3, "Usage: backup.py source_dir backup_dir"
    backup(sys.argv[1], sys.argv[2])
