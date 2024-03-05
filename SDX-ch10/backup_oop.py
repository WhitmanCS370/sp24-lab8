import csv
import shutil
import sys
import time
import json
from pathlib import Path

from hash_all import hash_all

# [base]
class Archive:
    def __init__(self, source_dir):
        self._source_dir = source_dir

    def backup(self):
        manifest = hash_all(self._source_dir)
        self._write_manifest(manifest)
        self._copy_files(manifest)
        return manifest
# [/base]


class ArchiveLocal(Archive):
    def __init__(self, source_dir, backup_dir, file_type):
        super().__init__(source_dir)
        self._backup_dir = backup_dir
        self.file_number = 0
        self.file_type = file_type

    def _copy_files(self, manifest):
        for (filename, hash_code) in manifest:
            source_path = Path(self._source_dir, filename)
            backup_path = Path(self._backup_dir, f"{hash_code}.bck")
            if not backup_path.exists():
                shutil.copy(source_path, backup_path)

    def _write_manifest(self, manifest):
        t = self._timestamp()
        backup_dir = Path(self._backup_dir)
        if not backup_dir.exists():
            backup_dir.mkdir()
        manifest_file = Path(backup_dir, f"{self.file_number}.{self.file_type}")
        self.file_number +=1
        with open(manifest_file, "w") as raw:
            if self.file_type == "json":
                json.dump(manifest, raw)
            else:
                writer = csv.writer(raw)
                writer.writerow(["filename", "hash"])
                writer.writerows(manifest)

    def _timestamp(self):
        return f"{time.time()}".split(".")[0]

def read_data(options):
    pass

def analyze_data(data):
    pass

def save_everything(result):
    pass

# [use]

def analyze_and_save(options, archiver):
    data = read_data(options)
    results = analyze_data(data)
    save_everything(results)
    archiver.backup()
# [/use]

if __name__ == "__main__":
    assert len(sys.argv) == 4, "Usage: backup.py source_dir backup_dir --json"
    source_dir = sys.argv[1]
    backup_dir = sys.argv[2]

    file_type = "csv"

    if sys.argv[3] == "--json":
        file_type == "json"

    # [create]
    archiver = ArchiveLocal(source_dir, backup_dir, file_type)
    # [/create]
    analyze_and_save({}, archiver)
