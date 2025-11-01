import pandas as pd

def analyze_data(df):
    print("Basic Stats : ")
    print(df.describe())

    print("\nTop 5 Highest Paid Players:")
    print(df.nlargest(5, "weekly_wages")[["name", "position", "weekly_wages", "goals", "assists"]])

    print("\nPlayers with Best Goals per Match Ratio:")
    df["goals_per_match"] = df["goals"] / df["matches"]
    print(df.nlargest(5, "goals_per_match")[["name", "position", "matches", "goals_per_match"]])

    correlation = df[["weekly_wages", "goals", "assists", "Age", "matches"]].corr()
    print("\nCorrelation Matrix:\n", correlation)
    return correlation

if __name__ == "__main__":
    df = pd.read_csv("data/processed/cleaned_data.csv")
    analyze_data(df)
