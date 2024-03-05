import csv
import shutil
import sys
from json import dumps
import time
from pathlib import Path

from hash_all import hash_all

# [base]
class Archive:
    def __init__(self, source_dir):
        self._source_dir = source_dir
        self.json = False

    def backup(self):
        manifest = hash_all(self._source_dir)
        if self.json:
            self._write_manifest_json(manifest)
        else:
            self._write_manifest(manifest)
        self._copy_files(manifest)
        return manifest
# [/base]


class ArchiveLocal(Archive):
    def __init__(self, source_dir, backup_dir):
        super().__init__(source_dir)
        self._backup_dir = backup_dir

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
        manifest_file = Path(backup_dir, f"{t}.csv")
        with open(manifest_file, "w") as raw:
            writer = csv.writer(raw)
            writer.writerow(["filename", "hash"])
            writer.writerows(manifest)

    def _timestamp(self):
        return f"{time.time()}".split(".")[0]
    
    def _write_manifest_json(self, manifest):
        t = self._timestamp()
        backup_dir = Path(self._backup_dir)
        if not backup_dir.exists():
            backup_dir.mkdir()
        manifest_file = Path(backup_dir, f"{t}.json")
        with open(manifest_file, "w") as raw:
            json_text = {}
            for item in manifest:
                json_text[str(item[0])] = f"{item[1]}"
            json_text = dumps(json_text)
            raw.write(json_text)
        

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
    assert len(sys.argv) >=3, "Usage: backup.py source_dir backup_dir"
    source_dir = sys.argv[1]
    backup_dir = sys.argv[2]
    archiver = ArchiveLocal(source_dir, backup_dir)
    if ((len(sys.argv) == 4) and sys.argv[3] == '-j'):
        archiver.json = True
    # [create]
    # [/create]
    analyze_and_save({}, archiver)
