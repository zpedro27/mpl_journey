import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import geopandas as gpd
from pypalettes import load_cmap
from drawarrow import ax_arrow
from highlight_text import ax_text

df = pd.read_csv("../../data/newyork-airbnb/newyork-airbnb.csv")

df_agg = (
    df["neighbourhood"]
    .value_counts()
    .head(10)
    .to_frame(name="count")
    .reset_index()
    .rename(columns={"index": "neighbourhood"})
    .sort_values("count")
)
labels = df_agg["neighbourhood"]
values = df_agg["count"]

fig, ax = plt.subplots(layout="tight")

# Display bars
color_map = {True: "darkgreen", False:"lightgray"}
color_map_text = {True: "white", False:"black"}

colors_bars = (labels=="Williamsburg").map(color_map)


ax.barh(y=labels, width=values, color=colors_bars)

# Add values on bars
for i, (value, nb) in enumerate(zip(values, labels)):
  ax.text(value-100, i-0.2, f"{value/1000 :.1f}k",
          color=color_map_text[nb=="Williamsburg"],
          horizontalalignment="right")

# Additional config
ax.spines[["top", "bottom", "right", "left"]].set_visible(False)
ax.tick_params("both", length=0)
ax.set_xticks([], [])
ax.set_title("New York neighborhood with the most Airbnbs", fontsize=14)

plt.savefig("image.png")
plt.show()




