import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize(df):

    plt.figure(figsize=(8,6))
    sns.scatterplot(x="weekly_wages", y="goals", hue="position", data=df)
    plt.title("Weekly Wages vs Goals")
    plt.savefig("wages_vs_goals.png")
    plt.close()

    plt.figure(figsize=(8,6))
    sns.scatterplot(x="weekly_wages", y="assists", hue="position", data=df)
    plt.title("Weekly Wages vs Assists")
    plt.savefig("wages_vs_assists.png")
    plt.close()

    plt.figure(figsize=(7,5))
    sns.heatmap(df[["weekly_wages", "annual_wages", "goals", "assists", "matches", "Age"]].corr(), annot=True, cmap="coolwarm")
    plt.title("Feature Correlation Heatmap")
    plt.savefig("feature_correlation_heatmap.png")
    plt.close()

if __name__ == "__main__":
    df = pd.read_csv("data/processed/cleaned_data.csv")
    visualize(df)
