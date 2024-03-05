import csv
import shutil
import sys
import time
from pathlib import Path
import json 

from hash_all import hash_all


# [backup]
def backup(source_dir, backup_dir, format):
    manifest = hash_all(source_dir)
    timestamp = current_time()
    write_manifest(backup_dir, timestamp, manifest, format)
    copy_files(source_dir, backup_dir, manifest)
    return manifest
# [/backup]

# [copy]
def copy_files(source_dir, backup_dir, manifest):
    for (filename, hash_code) in manifest:
        source_path = Path(source_dir, filename)
        backup_path = Path(backup_dir, "{}.bck".format(hash_code))
        if not backup_path.exists():
            shutil.copy(source_path, backup_path)
# [/copy]

# [time]
def current_time():
    return f"{time.time()}".split(".")[0]
# [/time]

# [write]
def write_manifest(backup_dir, timestamp, manifest, format):
    backup_dir = Path(backup_dir)
    if not backup_dir.exists():
        backup_dir.mkdir()
    manifest_file = Path(backup_dir, f"{timestamp}.{format}")
    with open(manifest_file, "w") as raw:
        writer = csv.writer(raw)
        writer.writerow(["filename", "hash"])
        writer.writerows(manifest)
# [/write]

if __name__ == "__main__":
    assert len(sys.argv) == 4, "Usage: backup.py source_dir backup_dir --format format"
    backup(sys.argv[1], sys.argv[2], sys.argv[4] == "CSV")
