import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/ADSLab-Salzburg/DataAnalysiswithPython/main/data/titanic.csv"
df = pd.read_csv(url)

# Calculate survival likelihood by class
survival_rate = df.groupby('Pclass')['Survived'].mean().reset_index()
survival_rate.columns = ['Pclass', 'Survival Rate']

# Create the plot
sns.set_style("darkgrid")
plt.figure(figsize=(8, 6))
bars = plt.bar(survival_rate['Pclass'], survival_rate['Survival Rate'], color=['green', 'orange', 'red'])

for bar, rate in zip(bars, survival_rate['Survival Rate']):
    plt.text(
        bar.get_x() + bar.get_width() / 2, # X-coordinate
        0.13,                              # Y-coordinate
        f"{rate:.1%}",                     # Convert to percentage with 1 decimal place
        ha='center',                       # Center align text
        fontsize=16,                       # Adjust font size
        color='white'                      # Text color
    )

plt.title('Survival Likelihood by Passenger Class', fontsize=14)
plt.xlabel('Passenger Class', fontsize=12)
plt.ylabel('Survival Rate', fontsize=12)
plt.xticks(ticks=[1, 2, 3], labels=['1st Class', '2nd Class', '3rd Class'], fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()