import csv
import shutil
import sys
import time
import pandas as pd
import json
from pathlib import Path

from hash_all import hash_all

SEQUENCE = 0

# [backup]
def backup(source_dir, backup_dir):
    manifest = hash_all(source_dir)
    SEQUENCE = SEQUENCE + 1
    write_manifest(backup_dir, manifest)
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
def write_manifest(backup_dir, manifest):
    backup_dir = Path(backup_dir)
    if not backup_dir.exists():
        backup_dir.mkdir()
    manifest_file = Path(backup_dir, f"{SEQUENCE}.csv")
    with open(manifest_file, "w") as raw:
        writer = csv.writer(raw)
        writer.writerow(["filename", "hash", "username"])
        writer.writerows(manifest)
# [/write]

if __name__ == "__main__":
    assert len(sys.argv) >= 3    #"Usage: backup.py source_dir backup_dir"
    manifest = backup(sys.argv[1], sys.argv[2])
    if len(sys.argv) == 4 and sys.argv[3] == "$BACKUPS":
        if sys.argv[4] == "JSON":
            with open(f"{SEQUENCE}.json", "w") as f:
                json.dump(manifest,f)
        elif sys.argv[4] == "CSV":
            df = pd.DataFrame.from_dict(manifest)
            df.to_csv(f"{SEQUENCE}.csv", index=True)