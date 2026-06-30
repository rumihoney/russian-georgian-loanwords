# This script reads the list of Georgian loanwords from Russian, which was saved as a JSON file in the previous step, 
# and creates a new dictionary with the specified structure. The new dictionary is then saved as a new JSON file for further use.

import json
with open("geo_borrowed_from_russian.json", encoding="utf-8") as f:
    titles = json.load(f)

# categories list:
categories = [
    "institutional",
    "military",
    "everyday",
    "culture",
    "economy",
    "religion",
    "other"
]

# generate the dictionary as a new json file
russian_loanwords = {}
for word in titles:
    russian_loanwords[word] = {
        "transliteration": "",
        "ipa": "",
        "russian": "",
        "english": "",
        "category": ""  
    }

# write the dictionary to a new json file
with open("dictionary_categories.json", "w", encoding="utf-8") as f:
    json.dump(russian_loanwords, f, ensure_ascii=False, indent=2)
