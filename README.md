# Russian Loanwords in Georgian

A computational linguistics project for LING 421 investigating Russian loanwords in Georgian. The project combines Python, Wiktionary data, and manual linguistic annotation to analyze lexical borrowing patterns across semantic categories.

## Project Structure

- **dataset.py** — Extracts Russian loanwords in Georgian from Wiktionary.
- **geo_borrowed_from_russian.json** — Raw dataset exported from Wiktionary.
- **russianloans_dictionary_structure.py** — Converts the raw dataset into a structured dictionary.
- **dictionary_categories.json** — Prototype dictionary containing categorized entries.
- **russianloans.py** — Manually annotated dataset of the first 100 loanwords.
- **data_analysis.py** — Calculates category frequencies and percentages.
- **full_report.docx** — Final written report describing the methodology and findings.

## Method

1. Extract Russian loanwords from Wiktionary.
2. Export the raw entries as a JSON dataset.
3. Build a structured dictionary from the extracted data.
4. Manually translate and categorize the first 100 loanwords.
5. Calculate category frequencies and percentages using Python.

## Results

The manually annotated dataset contained **100 Russian loanwords** grouped into semantic categories.

| Analysis | Output |
|----------|--------|
| Dataset size | 100 loanwords |
| Source | Wiktionary |
| Analysis | Category frequencies and percentages |
| Output | Frequency table and pie chart |

## Technologies

- Python
- Wiktionary
- JSON
