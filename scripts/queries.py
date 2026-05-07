import json # Import the json module to work with JSON data

# Open the scientists.json file in read mode with UTF-8 encoding

with open("./data/scientists.json", "r", encoding="utf-8") as f: 
    scientists = json.load(f)

# Print the names of all scientists in the dataset born in France.

print("\nScientists born in France:\n")

for scientist in scientists:
    if scientist["country"] == "France":
        print(scientist["name"])

# Print the names of all scientists who contributed to the field of computing.

print("\nScientists in Computing:\n")

for scientist in scientists:
    if any("comput" in field.lower() for field in scientist["fields"]):
        print(scientist["name"])

# Print the names of all scientists who have contributed to more than one field of research.

print("\nScientists with multiple fields:\n")

for scientist in scientists:
    if len(scientist["fields"]) > 1:
        print(scientist["name"], scientist["fields"])

# Update the death year of Mary Jackson to 2005.
import json

with open("./data/scientists.json", "r", encoding="utf-8") as f:
    scientists = json.load(f)

for scientist in scientists:
    if "Mary Jackson" in scientist["name"]:
        scientist["death_year"] = 2005

with open("./data/scientists.json", "w", encoding="utf-8") as f:
    json.dump(scientists, f, indent=4)

print("Mary Jackson updated")

#Print the names of all scientists who died before the age of 40.

print("\nScientists who died before 40:\n")

for scientist in scientists:

    if scientist["birth_year"] and scientist["death_year"]:

        age = scientist["death_year"] - scientist["birth_year"]

        if age < 40:
            print(scientist["name"], "Age:", age)

#Print names of the countries with the most scientists in the dataset.

print("\nCountries with most scientists:\n")

country_counts = {}

for scientist in scientists:
    country = scientist["country"]

    if country not in country_counts:
        country_counts[country] = 0

    country_counts[country] += 1

for country, count in sorted(country_counts.items(), key=lambda x: x[1], reverse=True):
    print(country, count)

#Print the names of all scientists who are still alive.

print("\nScientists still alive:\n")

for scientist in scientists:
    if scientist["death_year"] is None:
      print(scientist["name"])

#Print the names of all scientists who have contributed in NASA.

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

# Add a new event to the timeline of Margaret Hamilton's contributions to NASA, including the title "Apollo Guidance Software Contribution", the year 1965, the location "NASA", and a description "Worked on guidance software development".
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

# Update the year of the event "Apollo Guidance Software Contribution" in Margaret Hamilton's timeline to 1966.

for scientist in scientists:

    if scientist["name"] == "Margaret Hamilton":

        for event in scientist["events"]:

            if event["title"] == "Apollo Guidance Software Contribution":
                event["year"] = 1966

with open("./data/scientists.json", "w", encoding="utf-8") as f:
    json.dump(scientists, f, indent=4)

print("Event updated")

# Add a new scientist to the dataset with the name "Annie Easley", birth year 1933, death year 2011, country "USA", fields ["Computer Science", "Mathematics"], description "NASA computer scientist and mathematician who worked on rocket systems.", and an event with the title "Joined NASA", year 1955, location "NASA Lewis Research Center", and description "Started work as a computer scientist".

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