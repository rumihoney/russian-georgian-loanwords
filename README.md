# Russian Loanwords in Georgian

A computational linguistics project for **LING 421 – Non-Indo-European Structures: Kartvelian Linguistics** (Concordia University, Winter 2026) investigating Russian loanwords in Georgian using Python, Wiktionary, and manual linguistic annotation.

## Repository Structure

The repository is organized according to the stages of the project.

```text
russian-georgian-loanwords/
│
├── 01_data/
│   ├── dictionary_categories.json
│   └── geo_borrowed_from_russian.json
│
├── 02_scripts/
│   ├── dataset.py
│   ├── dictionary_structure.py
│   └── data_analysis.py
│
├── 03_notebooks/
│   ├── brainstorm.ipynb
│   ├── russianloans_analysis.ipynb
│   └── annotated_loans.py
│
├── 04_results/
│   └── loanword_category_results.csv
│
└── README.md
```

The project follows a reproducible workflow:

1. Extract Russian-derived Georgian terms from Wiktionary.
2. Structure and annotate the dataset.
3. Analyze semantic borrowing patterns.
4. Export the resulting data and statistics.

## Results

The final annotated dataset contains **100 Russian loanwords** grouped into semantic categories.

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

- Institutional and military vocabulary account for nearly half of the dataset.
- Everyday and cultural vocabulary are also common borrowing domains.
- Economic and religious loanwords occur less frequently.
- The results suggest that Russian lexical influence is concentrated primarily in institutional and military domains.

## Tools

- Python
- Jupyter Notebooks
- JSON
- Wiktionary

## Future Improvements

- Expand the dataset.
- Refine semantic categories.
- Incorporate corpus frequency data.
- Explore automatic semantic classification methods using NLP.
- Visualize results (matplotlib)
  
## Course

**LING 421 – Non-Indo-European Structures: Kartvelian Linguistics**  
Concordia University, Winter 2026
