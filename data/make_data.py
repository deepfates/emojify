import csv
import json

with open('personas.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    lines = dict(csv_reader)
    lines.pop('character')
    characters = {v: k for k, v in lines.items()}

with open("emojis.json", 'r') as f:
    emojis_raw = json.load(f)
emojis = {}
for k,v in emojis_raw.items():
    for o in v:
        keywords = " ".join(o["keywords"])
        full_description = f"{o['description']} {keywords}"
        unicode_char = f'{o["code"].replace("+", "000")}'
        emojis[full_description] = o["emoji"]

with open('data.py', 'w') as f:
    print("WRITING DATA")
    print("CHARACTERS = ", characters, file=f)
    print("EMOJIS = ", emojis, file=f)