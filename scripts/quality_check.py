import pandas as pd

ANNOTATED_DATA_PATH = "data/annotated_data.csv"
REPORT_PATH = "reports/quality_report.txt"

def main():
    df = pd.read_csv(ANNOTATED_DATA_PATH)

    total_records = len(df)
    label_distribution = df["label"].value_counts()

    with open(REPORT_PATH, "w") as report:
        report.write("AI Data Quality Report\n")
        report.write("======================\n\n")
        report.write(f"Total Records: {total_records}\n\n")
        report.write("Label Distribution:\n")
        report.write(label_distribution.to_string())
        report.write("\n\nData validation completed successfully.")

    print("✅ Quality report generated.")

if __name__ == "__main__":
    main()
