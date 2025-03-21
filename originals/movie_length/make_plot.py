import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import geopandas as gpd
from pypalettes import load_cmap
from drawarrow import ax_arrow
from highlight_text import ax_text

# Define palette:
colors = load_cmap("Antique").colors

# Load data:
df = pd.read_csv("../../data/netflix/netflix.csv")

# Select subset:
countries = [
  "India",
  "United States",
  "France",
  "United Kingdom",
]
df = df[df["country"].isin(countries)]

# Define figure:
fig, ax = plt.subplots(len(countries), 1, 
                       sharex=True,
                       layout="tight")
ax=ax.reshape(-1)

# Display distributions:
for i, (g, dfg) in enumerate(df.groupby("country")):
  sns.kdeplot(x=dfg["duration"],
              fill=True,
              color=colors[i],
              ax=ax[i],
             )

  xmed = dfg["duration"].median()
  _, ymax = ax[i].get_ylim()
  ax[i].text(xmed + 10,
             ymax*0.9,
             g,
             color=colors[i],
            )
  
  ax[i].axhline(0,
                linestyle="-",
                color="lightgray")
  
  ax[i].axvline(xmed,
                linestyle="--",
                color=colors[i])

  
  ax[i].spines[["bottom", "top", "left", "right"]].set_visible(False)
  ax[i].tick_params(length=0, labelcolor="lightgray")
  ax[i].set_yticks([])
  ax[i].set_ylabel("")
  
# Add labels:
fig.text(
  x=0.2,
  y=0.62,
  s="Indian movies\nlast longer!",
  ha="center",
  size=18
)
ax[-1].set_xlabel("Movie duration, using Netflix movies", color="gray")


plt.savefig("image.png")
plt.show()




