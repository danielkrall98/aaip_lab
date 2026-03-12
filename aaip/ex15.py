import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Shapefile
shapefile_path = "natural_earth_data/ne_110m_admin_0_countries.shp"
countries = gpd.read_file(shapefile_path)

# Population Density data from World Bank
world_data_path = "data/d1e3438c-014d-4250-bf31-1f534f35550a_Data.csv"
worldbank_data = pd.read_csv(world_data_path)

year = 2021
density = worldbank_data[["Country Code", f"{year} [YR{year}]"]].rename(columns={f"{year} [YR{year}]": "Population Density"})

# Merge data with dataframe
countries = countries.merge(
    density,
    left_on="ISO_A3",           # Column in the shapefile
    right_on="Country Code",    # Column in the World Bank data
    how="left"
)

# Plot the data for Asia
asia = countries[countries["CONTINENT"] == "Asia"]
asia["Population Density"] = pd.to_numeric(asia["Population Density"], errors="coerce")

asia.plot(column="Population Density",
          figsize=(15, 10),
          cmap="RdYlBu_r",
          legend=True,
          edgecolor="black",
          missing_kwds={"color": "lightgrey", "label": "No Data"})

plt.title(f"Population Density in Asia ({year})", fontsize=16)
plt.show()