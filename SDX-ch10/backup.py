import csv
from glob import glob
import json
import shutil
import sys
import time
from pathlib import Path

from hash_all import hash_all

def get_next_number():
    with open("number.txt", "r") as f:
        num = int(f.readline())
    with open("number.txt", "w") as f:
        f.write(str(num + 1))
    
    return str(num + 10 ** 10)[1:]


# [backup]
def backup(source_dir, backup_dir, save_json=False):
    manifest = hash_all(source_dir)
    backup_number = get_next_number()
    if save_json:
        write_manifest_json(backup_dir, backup_number, manifest)
    else:
        write_manifest_csv(backup_dir, backup_number, manifest)
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
def write_manifest_csv(backup_dir, backup_num, manifest):
    backup_dir = Path(backup_dir)
    if not backup_dir.exists():
        backup_dir.mkdir()
    manifest_file = Path(backup_dir, f"{backup_num}.csv")
    with open(manifest_file, "w") as raw:
        writer = csv.writer(raw)
        writer.writerow(["filename", "hash"])
        writer.writerows(manifest)
# [/write]

def write_manifest_json(backup_dir, backup_num, manifest):
    backup_dir = Path(backup_dir)
    if not backup_dir.exists():
        backup_dir.mkdir()
    manifest_file = Path(backup_dir, f"{backup_num}.json")
    with open(manifest_file, "w") as raw:
        json.dump(manifest, raw)

def convert_from_csv_to_json_data_migration_function_command(backup_file):
    manifest_file = Path(str(backup_file)[:-4] + ".json")
    backup_file = Path(backup_file)
    with open(backup_file, 'r') as f:
        reader = csv.reader(f)
        rows = []
        for row in reader:
            rows.append(row)

    rows = rows[1:]

    with open(manifest_file, "w") as raw:
        json.dump(rows, raw)

def do_ALL_of_them(backup_dir):
    backup_dir = Path(backup_dir)
    for name in glob("**/*.*", root_dir=backup_dir, recursive=True):
        full_name = Path(backup_dir, name)
        convert_from_csv_to_json_data_migration_function_command(full_name)


if __name__ == "__main__":
    assert len(sys.argv) < 5, "Usage: backup.py source_dir backup_dir save_json"
    if sys.argv[1] == "migrate_stuff":
        do_ALL_of_them(sys.argv[2])
    elif len(sys.argv) < 4:
        backup(sys.argv[1], sys.argv[2], False)
    else:
        should_I_save_json_or_not_boolean_flag = sys.argv[3] == "True"
        backup(sys.argv[1], sys.argv[2], should_I_save_json_or_not_boolean_flag)
