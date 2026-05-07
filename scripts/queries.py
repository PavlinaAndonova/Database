import json

with open("./data/scientists.json", "r", encoding="utf-8") as f:
    scientists = json.load(f)

print("\nScientists born in France:\n")

for scientist in scientists:
    if scientist["country"] == "France":
        print(scientist["name"])

print("\nScientists in Computing:\n")

for scientist in scientists:
    if any("comput" in field.lower() for field in scientist["fields"]):
        print(scientist["name"])

print("\nScientists with multiple fields:\n")

for scientist in scientists:
    if len(scientist["fields"]) > 1:
        print(scientist["name"], scientist["fields"])

import json

with open("./data/scientists.json", "r", encoding="utf-8") as f:
    scientists = json.load(f)

for scientist in scientists:
    if "Mary Jackson" in scientist["name"]:
        scientist["death_year"] = 2005

with open("./data/scientists.json", "w", encoding="utf-8") as f:
    json.dump(scientists, f, indent=4)

print("Mary Jackson updated")

print("\nScientists who died before 40:\n")

for scientist in scientists:

    if scientist["birth_year"] and scientist["death_year"]:

        age = scientist["death_year"] - scientist["birth_year"]

        if age < 40:
            print(scientist["name"], "Age:", age)

print("\nCountries with most scientists:\n")

country_counts = {}

for scientist in scientists:
    country = scientist["country"]

    if country not in country_counts:
        country_counts[country] = 0

    country_counts[country] += 1

for country, count in sorted(country_counts.items(), key=lambda x: x[1], reverse=True):
    print(country, count)

print("\nScientists still alive:\n")

for scientist in scientists:
    if scientist["death_year"] is None:
      print(scientist["name"])

print("\nScientists connected to NASA:\n")

for scientist in scientists:
    if "nasa" in scientist["description"].lower():
        print(scientist["name"])

print("\nWhich countries have the most fields of research contributions:\n")
country_fields = {}

for scientist in scientists:

    country = scientist["country"]

    if country not in country_fields:
        country_fields[country] = set()

    for field in scientist["fields"]:
        country_fields[country].add(field)

results = []

for country, fields in country_fields.items():
    results.append((country, len(fields)))

for result in sorted(results, key=lambda x: x[1], reverse=True):
    print(result)


import json

with open("./data/scientists.json", "r", encoding="utf-8") as f:
    scientists = json.load(f)

new_event = {
    "title": "Apollo Guidance Software Contribution",
    "year": 1965,
    "location": "NASA",
    "description": "Worked on guidance software development"
}

for scientist in scientists:
    if scientist["name"] == "Margaret Hamilton":
        scientist["events"].append(new_event)

with open("./data/scientists.json", "w", encoding="utf-8") as f:
    json.dump(scientists, f, indent=4)

print("Event added")

for scientist in scientists:

    if scientist["name"] == "Margaret Hamilton":

        for event in scientist["events"]:

            if event["title"] == "Apollo Guidance Software Contribution":
                event["year"] = 1966

with open("./data/scientists.json", "w", encoding="utf-8") as f:
    json.dump(scientists, f, indent=4)

print("Event updated")

import json

with open("./data/scientists.json", "r", encoding="utf-8") as f:
    scientists = json.load(f)

new_scientist = {
    "name": "Annie Easley",
    "birth_year": 1933,
    "death_year": 2011,
    "country": "USA",
    "fields": ["Computer Science", "Mathematics"],
    "description": "NASA computer scientist and mathematician who worked on rocket systems.",
    "events": [
        {
            "title": "Joined NASA",
            "year": 1955,
            "location": "NASA Lewis Research Center",
            "description": "Started work as a computer scientist"
        }
    ]
}

scientists.append(new_scientist)

with open("./data/scientists.json", "w", encoding="utf-8") as f:
    json.dump(scientists, f, indent=4)

print("Scientist added")