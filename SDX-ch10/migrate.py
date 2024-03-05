import pandas as pd
import os
from pathlib import Path

def migrate(dirname):
    for filename in os.listdir(dirname):
        df = pd.read_csv(filename)
        js = df.to_json()
        new_file = Path(dirname, filename.strip(".")[0].append(".json"))
        with open(new_file, "w") as raw:
            raw.write(js)