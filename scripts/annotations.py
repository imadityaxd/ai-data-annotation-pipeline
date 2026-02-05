import pandas as pd

CLEANED_DATA_PATH = "data/cleaned_data.csv"
ANNOTATED_DATA_PATH = "data/annotated_data.csv"

def annotate_review(text: str) -> str:
    """
    Rule-based annotation logic.
    This simulates deterministic labeling used in AI data pipelines.
    """
    positive_keywords = ["amazing", "excellent", "great", "perfect"]
    negative_keywords = ["bad", "terrible", "waste"]

    if any(word in text for word in positive_keywords):
        return "Positive"
    elif any(word in text for word in negative_keywords):
        return "Negative"
    return "Neutral"

def main():
    df = pd.read_csv(CLEANED_DATA_PATH)

    # Apply annotation logic
    df["label"] = df["cleaned_text"].apply(annotate_review)

    # Save annotated dataset
    df.to_csv(ANNOTATED_DATA_PATH, index=False)

    print("✅ Data annotation completed successfully.")

if __name__ == "__main__":
    main()
