import csv
import sys
from json import dumps
from pathlib import Path

def convert_to_json(csvfile):
    with open(csvfile) as file_obj: 
        reader_obj = csv.reader(file_obj) 
        json_dict = {}
        json_file = Path("./backups", csvfile.split("/")[-1][:-4] + ".json")
        #json_file = Path(csvfile[:-5], ".json")
        with open(json_file, "w") as raw:
            for row in reader_obj: 
                json_dict[str(row[0])] = f"{row[1]}"
            json_dict = dumps(json_dict)
            raw.write(json_dict)

if __name__ == "__main__":
    convert_to_json(sys.argv[1])