# AI Data Quality & Annotation Pipeline

This project implements an end-to-end AI data preparation pipeline designed to clean, annotate, and validate text datasets used for training machine learning and LLM systems.

## Features
- Cleans raw text data by removing duplicates and missing values
- Normalizes text for consistency
- Annotates data using rule-based labeling
- Performs dataset quality validation
- Generates a structured quality report

## Tech Stack
- Python
- Pandas

## Use Case
High-quality training data is critical for reliable AI systems. This project simulates real-world AI data workflows used before model training or fine-tuning.

## How to Run
```bash
python scripts/data_cleaning.py
python scripts/annotation.py
python scripts/quality_check.py
