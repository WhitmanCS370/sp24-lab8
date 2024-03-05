import csv
import json

def csv_to_json(csv_file, json_file="new"):
    manifests = []
   
    with open(csv_file, 'r') as s:
        csvreader = csv.DictReader(s)
        for row in csvreader:
            manifests.append(row)
   
    with open(json_file, 'w') as s:
        json.dump(manifests, s)