# Data for Cultural Object Description Simplification Evaluation

This folder contains datasets used to evaluate the simplification capabilities of two Large Language Models (LLMs) on texts derived from cultural object descriptions.

## Files

1. `3000_HistoricOrArtisticProperty.jsonl`
   - Contains 3000 cultural objects extracted from ArCO
   - Fields:
     - nome (name)
     - data (date)
     - materiale (material)
     - locus
     - description
     - url

2. `processed_3000_HistoricOrArtisticProperty.tsv`
   - Includes all fields from the JSONL file
   - Additional calculated metrics for each description:
     - Gulpease Index
     - Flesch Reading Ease Score
     - Word count of fundamental vocabulary words


## LLM Evaluation

For the evaluation of the LLMs, we used a subsample of the original dataset (`3000_HistoricOrArtisticProperty.jsonl`). Specifically, we used the first 200 descriptions from this dataset to test the simplification capabilities of Claude Sonnet 3.5 and GPT-4. The results of this evaluation are contained in the output folder.


## Usage

These datasets are intended for researchers and developers interested in:
- Natural Language Processing (NLP) in the cultural heritage domain
- Text simplification techniques
- Evaluation of LLM performance on specialized texts

## Data Source

The original cultural object data is sourced from ArCO (Architecture of Knowledge).

## Notes

- The JSONL and TSV formats are used for easy parsing and analysis.
- Researchers are encouraged to refer to the methodology used for calculating readability indices and fundamental vocabulary word counts.

For any questions or additional information, please open an issue in this repository.
