import pandas as pd
import matplotlib.pyplot as plt

world_data_path = "data/API_IT.NET.USER.ZS_DS2_en_csv_v2_2160.csv"
worldbank_data = pd.read_csv(world_data_path, skiprows=4)

austria_data = worldbank_data[worldbank_data["Country Name"] == "Austria"]

# Dataset to long format (columns -> rows)
austria_melted = austria_data.melt(
    id_vars="Country Name",
    var_name="Year",
    value_name="Internet Usage (%)"
)

# to numeric (invalid values to NaN)
austria_melted["Year"] = pd.to_numeric(austria_melted["Year"], errors="coerce")
austria_melted = austria_melted.dropna(subset=["Year"])

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(austria_melted["Year"], austria_melted["Internet Usage (%)"], marker="o", color="red", label="Internet Usage (%)")
plt.title("Internet Usage in Austria Over Time", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Internet Usage (%)", fontsize=14)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()

plt.show()