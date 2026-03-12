import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/ADSLab-Salzburg/DataAnalysiswithPython/main/data/titanic.csv"
df = pd.read_csv(url)

df = df.dropna(subset=['Sex'])

# Calculate survival rates for each class and gender
survival_rates = df.groupby(['Pclass', 'Sex'])['Survived'].mean().reset_index()

# Plotting
palette = {'male': 'skyblue', 'female': 'salmon'}
plt.figure(figsize=(10, 6))
sns.barplot(data=survival_rates, x='Pclass', y='Survived', hue='Sex', palette=palette, edgecolor='black')

plt.title("Gender Survival Comparison Across Classes", fontsize=16)
plt.xlabel("Passenger Class", fontsize=12)
plt.ylabel("Survival Rate", fontsize=12)
plt.ylim(0, 1)
plt.xticks(ticks=[0, 1, 2], labels=["1st Class", "2nd Class", "3rd Class"])
plt.legend(title="Sex", fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

for bar in plt.gca().patches:
    height = bar.get_height()
    if height > 0:
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height - 0.1,
            f"{height:.0%}",
            ha='center',
            va='bottom',
            fontsize=12
        )

plt.tight_layout()
plt.show()