import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import geopandas as gpd
from pypalettes import load_cmap
from drawarrow import ax_arrow
from highlight_text import ax_text
import cartopy.crs as ccrs

# Get data:
world = gpd.read_file("../../data/world/world.geojson")
world = world[world["name"] != "Antarctica"]

df = pd.read_csv("../../data/earthquakes/earthquakes.csv")
df = df.sort_values("Depth", ascending=False)


# Change projection:
projection = ccrs.Mercator()
previous_proj = ccrs.PlateCarree()  # default projection
world = world.to_crs(projection.to_proj4())

new_coords = projection.transform_points(
  previous_proj,
  df["Longitude"],
  df["Latitude"]
)
x = new_coords[:, 0]  # new longitude
y = new_coords[:, 1]  # new latitude


# Define bubble size:
min_s = 10
max_s = 1000
s = df["Depth"]
s = min_s + (s - s.min()) * (max_s - min_s) / (s.max() - s.min())

bubble_color = "#8880c8"


# Display map:
fig, ax = plt.subplots(subplot_kw={"projection": projection}, layout="tight")
world.plot(ax=ax, color="#aeadad", linewidth=0)


# Add bubbles:
scatter = ax.scatter(
    x, y, s=s, alpha=0.4, color=bubble_color, edgecolor="black", linewidth=0.5
)

# Add legend:
handles, labels = scatter.legend_elements(
    prop="sizes",
    alpha=0.6,
    color=bubble_color,
    num=3,
)
ax.legend(
    handles,
    labels,
    loc=(0.9, 0.9),
    framealpha=0,
)

ax.axis("off")
fig.text(x=1, y=0.97, s="Depth (in km)", ha="right")
fig.text(x=0.5, y=1, s="Earthquakes around the world", ha="center", size=15)


plt.savefig("image.png")
plt.show()




