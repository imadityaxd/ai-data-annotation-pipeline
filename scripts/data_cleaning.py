import pandas as pd
import re

RAW_DATA_PATH = "data/raw_data.csv"
CLEANED_DATA_PATH = "data/cleaned_data.csv"

def clean_text(text: str) -> str:
    """
    Normalize text for AI training by:
    - Lowercasing
    - Removing special characters
    """
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text.strip()

def main():
    # Load raw dataset
    df = pd.read_csv(RAW_DATA_PATH)

    # Remove rows with missing review text
    df = df.dropna(subset=["review_text"])

    # Remove duplicate reviews
    df = df.drop_duplicates(subset=["review_text"])

    # Apply text normalization
    df["cleaned_text"] = df["review_text"].apply(clean_text)

    # Save cleaned dataset
    df.to_csv(CLEANED_DATA_PATH, index=False)

    print("✅ Data cleaning completed successfully.")

if __name__ == "__main__":
    main()
