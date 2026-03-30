import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load data
temperature_data = pd.read_csv("data/temperature.csv")
co2_data = pd.read_csv("data/carbon_emmission.csv")

# Prepare data
temperature_years = temperature_data.filter(regex="^F").mean(axis=0)
temperature_years.index = temperature_years.index.str.replace("F", "").astype(int)

co2_data["Year"] = co2_data["Date"].str[:4].astype(int)
co2_yearly = co2_data.groupby("Year")["Value"].mean()

merged_data = pd.DataFrame(
    {"Temperature Change": temperature_years, "CO2 Concentration": co2_yearly}
).dropna()

import os

os.makedirs("images", exist_ok=True)

# 1. Time Series Plot
fig, ax1 = plt.subplots(figsize=(14, 6))

color = "tab:red"
ax1.set_xlabel("Year")
ax1.set_ylabel("Temperature Change (°C)", color=color)
ax1.plot(
    temperature_years.index,
    temperature_years.values,
    color=color,
    marker="o",
    label="Temperature Change (°C)",
)
ax1.tick_params(axis="y", labelcolor=color)

ax2 = ax1.twinx()
color = "tab:blue"
ax2.set_ylabel("CO₂ Concentration (ppm)", color=color)
ax2.plot(
    co2_yearly.index,
    co2_yearly.values,
    color=color,
    linestyle="--",
    marker="s",
    label="CO₂ Concentration (ppm)",
)
ax2.tick_params(axis="y", labelcolor=color)

plt.title("Time-series of Temperature Change and CO₂ Concentrations")
fig.tight_layout()
plt.savefig("images/time_series_plot.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved: time_series_plot.png")

# 2. Correlation Heatmap
fig, ax = plt.subplots(figsize=(6, 5))
corr = merged_data.corr()
im = ax.imshow(corr, cmap="RdBu", vmin=-1, vmax=1)
ax.set_xticks(range(len(corr.columns)))
ax.set_yticks(range(len(corr.columns)))
ax.set_xticklabels(corr.columns, rotation=45, ha="right")
ax.set_yticklabels(corr.columns)

for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        text = ax.text(
            j,
            i,
            f"{corr.iloc[i, j]:.2f}",
            ha="center",
            va="center",
            color="black",
            fontsize=12,
        )

plt.colorbar(im, ax=ax)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("images/correlation_heatmap.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved: correlation_heatmap.png")

# 3. Scatter Plot
plt.figure(figsize=(8, 6))
plt.scatter(
    merged_data["CO2 Concentration"],
    merged_data["Temperature Change"],
    alpha=0.7,
    c="steelblue",
    s=50,
)
plt.xlabel("CO₂ Concentration (ppm)")
plt.ylabel("Temperature Change (°C)")
plt.title("Temperature Change vs CO₂ Concentration")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("images/scatter_plot.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved: scatter_plot.png")

# 4. Trends Plot
temp_trend = linregress(temperature_years.index, temperature_years.values)
temp_trend_line = temp_trend.slope * temperature_years.index + temp_trend.intercept

co2_trend = linregress(co2_yearly.index, co2_yearly.values)
co2_trend_line = co2_trend.slope * co2_yearly.index + co2_trend.intercept

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

ax1.plot(
    temperature_years.index,
    temperature_years.values,
    "r-o",
    markersize=4,
    label="Temperature Change (°C)",
)
ax1.plot(
    temperature_years.index,
    temp_trend_line,
    "r--",
    linewidth=2,
    label=f"Trend (Slope: {temp_trend.slope:.2f})",
)
ax1.set_xlabel("Year")
ax1.set_ylabel("Temperature Change (°C)")
ax1.set_title("Temperature Trend")
ax1.legend()
ax1.grid(True, alpha=0.3)

ax2.plot(
    co2_yearly.index,
    co2_yearly.values,
    "b-o",
    markersize=4,
    label="CO₂ Concentration (ppm)",
)
ax2.plot(
    co2_yearly.index,
    co2_trend_line,
    "b--",
    linewidth=2,
    label=f"Trend (Slope: {co2_trend.slope:.2f})",
)
ax2.set_xlabel("Year")
ax2.set_ylabel("CO₂ Concentration (ppm)")
ax2.set_title("CO₂ Concentration Trend")
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.suptitle("Trends in Temperature Change and CO₂ Concentrations", fontsize=14)
plt.tight_layout()
plt.savefig("images/trends_plot.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved: trends_plot.png")

# 5. Seasonal Variation
co2_data["Month"] = co2_data["Date"].str[-2:].astype(int)
co2_monthly = co2_data.groupby("Month")["Value"].mean()

plt.figure(figsize=(10, 5))
months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]
plt.plot(range(1, 13), co2_monthly.values, "g-o", markersize=8)
plt.xticks(range(1, 13), months)
plt.xlabel("Month")
plt.ylabel("CO₂ Concentration (ppm)")
plt.title("Seasonal Variations in CO₂ Concentrations")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("images/seasonal_variation.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved: seasonal_variation.png")

# 6. Clustering Plot
clustering_data = merged_data[["Temperature Change", "CO2 Concentration"]].dropna()
scaler = StandardScaler()
scaled_data = scaler.fit_transform(clustering_data)

kmeans = KMeans(n_clusters=3, random_state=42)
clustering_data["Cluster"] = kmeans.fit_predict(scaled_data)

colors = ["green", "orange", "blue"]
labels = {0: "Moderate Temp & CO₂", 1: "High Temp & CO₂", 2: "Low Temp & CO₂"}

plt.figure(figsize=(10, 7))
for cluster in range(3):
    mask = clustering_data["Cluster"] == cluster
    plt.scatter(
        clustering_data.loc[mask, "CO2 Concentration"],
        clustering_data.loc[mask, "Temperature Change"],
        c=colors[cluster],
        label=labels[cluster],
        s=60,
        alpha=0.7,
    )

plt.xlabel("CO₂ Concentration (ppm)")
plt.ylabel("Temperature Change (°C)")
plt.title("Clustering of Years Based on Climate Patterns")
plt.legend(title="Climate Pattern")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("images/clustering_plot.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved: clustering_plot.png")

print("\n✅ All PNG files saved successfully!")
