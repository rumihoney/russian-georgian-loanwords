# This script queries the Wiktionary API to get all pages in the category "Georgian terms borrowed from Russian".
# It handles pagination and saves the results to a JSON file.
import requests
import json
import time

API = "https://en.wiktionary.org/w/api.php"
CATEGORY = "Category:Georgian_terms_borrowed_from_Russian"

headers = {
    "User-Agent": "RumiLoanwordProject/1.0 (learning; contact: none)"
}

all_titles = []
cmcontinue = None

while True:
    params = {
        "action": "query",
        "list": "categorymembers",
        "cmtitle": CATEGORY,
        "cmlimit": "500",         
        "format": "json",
        "formatversion": "2",
    }

    if cmcontinue:
        params["cmcontinue"] = cmcontinue

    r = requests.get(API, params=params, headers=headers, timeout=30)
    r.raise_for_status()
    data = r.json()

    members = data["query"]["categorymembers"]
    for item in members:
        all_titles.append(item["title"])

    print("Got so far:", len(all_titles))

    # If there's a next page, save the bookmark and loop again
    if "continue" in data:
        cmcontinue = data["continue"]["cmcontinue"]
        time.sleep(0.2)  # tiny nap to be polite
    else:
        break

print("TOTAL:", len(all_titles))

# Save to a file so you never have to re-download
with open("geo_borrowed_from_russian.json", "w", encoding="utf-8") as f:
    json.dump(all_titles, f, ensure_ascii=False, indent=2)

print("Saved: geo_borrowed_from_russian.json")
