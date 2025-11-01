import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    df = df.drop_duplicates().dropna()

    df = df[df["weekly_wages"] > 0]
    df = df[df["matches"] > 0]

    df["Age"] = df["Age"].astype(int)
    df["matches"] = df["matches"].astype(int)
    df["weekly_wages"] = df["weekly_wages"].astype(int)
    df["annual_wages"] = df["annual_wages"].astype(int)

    df = df.replace('-', 0)

    df["goals"] = df["goals"].astype(int)
    df["assists"] = df["assists"].astype(int)

    return df

if __name__ == "__main__":
    df = load_data("data/raw/merged.csv")
    df_clean = clean_data(df)
    df_clean.to_csv("data/processed/cleaned_data.csv", index=False)
