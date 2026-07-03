# Russian Loanwords in Georgian

A computational linguistics project for LING 421 investigating Russian loanwords in Georgian. The project combines Python, Wiktionary data, and manual linguistic annotation to analyze lexical borrowing patterns across semantic categories.

## Project Structure

- **dataset.py** — Extracts Georgian terms derived from Russian from Wiktionary.
- **geo_borrowed_from_russian.json** — Raw dataset exported from Wiktionary.
- **dictionary_structure.py** — Converts the raw dataset into a structured Python dictionary.
- **dictionary_categories.json** — Prototype categorized dataset used during development.
- **russianloans.py** — Final manually annotated dataset.
- **data_analysis.py** — Python script for analyzing the annotated dataset.
- **russianloans_analysis.ipynb** — Jupyter Notebook containing the complete analysis workflow and results.
- **README.md** — Project documentation.

## Method

1. Extract Russian-derived Georgian terms from Wiktionary.
2. Export the extracted entries as a JSON dataset.
3. Convert the raw data into a structured dictionary.
4. Manually annotate the final dataset with linguistic information.
5. Analyze semantic category frequencies using Python.
6. Present the results in a Jupyter Notebook.

## Results

The manually annotated dataset contained **100 Russian loanwords** grouped into semantic categories.

| Category | Count | Percentage |
|----------|------:|-----------:|
| Institutional | 26 | 26% |
| Military | 23 | 23% |
| Everyday | 17 | 17% |
| Culture | 14 | 14% |
| Other | 11 | 11% |
| Economy | 6 | 6% |
| Religion | 3 | 3% |

### Key Findings

- Institutional vocabulary represents the largest semantic category (26%).
- Military terminology is also highly represented (23%), reflecting historical Russian-Georgian military contact.
- Everyday and cultural vocabulary account for 17% and 14% of the dataset, respectively.
- Economy (6%) and religion (3%) are comparatively less frequent sources of lexical borrowing.
- Overall, the dataset suggests that Russian loanwords are concentrated primarily in institutional and military domains.


## Technologies

- Python
- Jupyter Notebook
- JSON
- Wiktionary

## Future Improvements

- Expand the dataset beyond 100 loanwords.
- Refine and standardize semantic category definitions.
- Add data visualizations (e.g., bar charts and pie charts).
- Export analysis results automatically to CSV or Excel.
- Incorporate corpus frequency data to compare dictionary entries with real language use.
- Explore automatic semantic classification methods using NLP.
