import pandas as pd
import json

# Read Excel file
file_path = "../data/HistoricalSTEM.xlsx"

df = pd.read_excel(file_path)

scientists = []

for _, row in df.iterrows():

    lived = str(row["Lived"])
    years = lived.split("-")

    birth_year = None
    death_year = None

    if len(years) == 2:
        birth_year = int(years[0].strip())

        death_text = years[1].strip()

        if death_text.lower() != "present":
            death_year = int(death_text)

    fields = [x.strip() for x in str(row["Main Area"]).split(",")]

    scientist = {
        "name": row["Name"],
        "birth_year": birth_year,
        "death_year": death_year,
        "country": row["Country of Birth"],
        "fields": fields,
        "description": str(row[df.columns[4]]),
        "events": []
    }

    scientists.append(scientist)

# Save to JSON file
with open("../data/scientists.json", "w", encoding="utf-8") as f:
    json.dump(scientists, f, indent=4)

print("JSON database created successfully")