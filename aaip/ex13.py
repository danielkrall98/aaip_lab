import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Shapefile
shapefile_path = "natural_earth_data/ne_110m_admin_0_countries.shp"
countries = gpd.read_file(shapefile_path)

# Internet usage data from World Bank
world_data_path = "data/API_IT.NET.USER.ZS_DS2_en_csv_v2_2160.csv"
worldbank_data = pd.read_csv(world_data_path, skiprows=4)

year = 2020
internet_usage = worldbank_data[["Country Name", f"{year}"]].rename(columns={f"{year}": "InternetUsage"})

# Merge data with dataframe
countries = countries.merge(
    internet_usage,
    left_on="NAME",             # Column in the shapefile
    right_on="Country Name",    # Column in the World Bank data
    how="left"
)

# Plot the data for Europe
europe = countries[countries["CONTINENT"] == "Europe"]

europe.plot(column="InternetUsage",
          figsize=(15, 10),
          cmap="coolwarm",
          legend=True,
          edgecolor="black",
          missing_kwds={"color": "lightgrey", "label": "No Data"}
)

plt.title(f"Internet Usage in Europe ({year})", fontsize=16)
plt.show()

# Correct wrong names
#name_corrections = {
#    "TURKEY": "TURKIYE"
#}