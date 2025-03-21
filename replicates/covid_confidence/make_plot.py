import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import geopandas as gpd
from pypalettes import load_cmap
from drawarrow import ax_arrow
from highlight_text import ax_text

df= pd.read_csv("../../data/economic/economic.csv")
df = df.loc[df.date == "2020-04-01"]

f, ax = plt.subplots()
f.set_facecolor("#3f3f3f")
ax.set_facecolor("#3f3f3f")

# Add title:
f.subplots_adjust(top=0.85)
f.text(x=0.5, y=0.9,
       s="Unemployment rates and Consumer confidence\nduring peak COVID-19 (April 2020)",
       fontsize=14,
       color="white",
       weight="bold",
       ha="center")


# Display data:
ax.scatter(x=df["consumer confidence"],
           y=df["unemployment rate"],
           color="#a2a2bf",
           edgecolor="white",
           s=600)

# Annotate:
for i, row in df.iterrows():
  ax.text(row["consumer confidence"]+7,
          row["unemployment rate"],
          row["country"].capitalize(),
          color="white", 
          ha="left", va="top")

# Add aix labels:
text_params = {"transform": ax.transAxes,
               "fontsize": 6,
               "color": "white", 
               "style": "italic"}
ax.text(x=0.95, y=0.05, s="Consumer confidence",
        ha="right", **text_params)
ax.text(x=0.05, y=0.9, s="Unemployment rates",
        ha="left", **text_params)


# Spines with arrows
ax.spines[["top", "right", "bottom", "left"]].set_visible(False)
ax.tick_params(labelcolor="white", length=0)
params = {"tail_position": [-52, 1.7],
          "color": "white",
          "fill_head": False,
          "ax": ax,
         }
ax_arrow(head_position=[-52, 15], **params)
ax_arrow(head_position=[125, 1.7], **params)

# Additional settings
ax.set_xlim([-55, 130])
ax.set_ylim([1.5, 15.9])

plt.savefig("image.png")
plt.show()




