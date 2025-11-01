from src.dataprerocessing import load_data, clean_data
from src.dataAnalysis import analyze_data
from src.dataVisualisation import visualize

if __name__ == "__main__":
    print("Running Football Wage vs Stats Analysis : ")

    df_raw = load_data("data/raw/merged.csv")
    df_clean = clean_data(df_raw)
    df_clean.to_csv("data/processed/cleaned_data.csv", index=False)

    analyze_data(df_clean)
    visualize(df_clean)

    print("Analysis complete!")