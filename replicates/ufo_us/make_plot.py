import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import geopandas as gpd
from pypalettes import load_cmap
from drawarrow import ax_arrow
from highlight_text import ax_text

# Read data:
world = gpd.read_file("../../data/world/world.geojson")
ufo = pd.read_csv("../../data/ufo/ufo.csv")

# Create figure:
fig, ax = plt.subplots(layout="tight")
fig.set_facecolor("#1b1e44")
ax.set_facecolor("#1b1e44")

# Display map:
world.plot(ax=ax, color="lightgray")

# Show UFO sightings:
sizes = ufo["duration"].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
ax.scatter(ufo["longitude"], ufo["latitude"],
           s=100*sizes,
           edgecolor="black",
           color="#8c90c0", alpha=0.6)

# Add title:
ax.text(0.5, 0.85,
        "Reports of unidentified flying objects in 2012",
        color="white", fontsize=12,
        ha="center",
        transform=ax.transAxes)

# Additional settings:
ax.set_xlim([-130, -60])
ax.set_ylim([20, 55])
ax.axis("off")

plt.savefig("image.png")
plt.show()




