import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import geopandas as gpd
from pypalettes import load_cmap
from drawarrow import ax_arrow
from highlight_text import ax_text, fig_text

# Load data:
df = pd.read_csv("../../data/natural-disasters/natural-disasters.csv")

# Define palette:
colors = load_cmap("Antique").colors

# Order of natural disasters:
disasters = ["Flood", "Extreme weather", "Earthquake",
             "Extreme temperature", "Drought", "Wet mass movement"]

# Define figure:
f, ax = plt.subplots(2, 3, figsize=(15, 10),
                     sharex=True, sharey=True)
ax = ax.reshape(-1)

# Display data:
for i, col in enumerate(disasters):
  df[["Year"] + disasters].plot("Year",
                                color="lightgray", alpha=0.4,
                                label=False, legend=False,
                                ax=ax[i])
  ax[i].plot(df["Year"], df[col],
             color=colors[i],
             linewidth=3)

  ax[i].text(1961, 160, col,
             weight="bold", fontsize=20,
             ha="left", va="center",
             color=colors[i])
  
  if i%3 == 0:
    ax[i].spines[["right", "top"]].set_visible(False)
  else:
    ax[i].spines[["right", "left", "top"]].set_visible(False)

  ax[i].tick_params("both", length=0)
  ax[i].set_xlabel("")
  
# Add title:
f.subplots_adjust(hspace=.5)
fig_text(x=0.5, y=0.5,
         s="<Flood> and <Extreme Weather> are the most\nfrequent natural disasters since the 60s",
         fontsize=25, ha="center", va="center",
         weight="bold",
       highlight_textprops=[
       {"color": colors[0], "weight": "bold"},
       {"color": colors[1], "weight": "bold"},])


plt.savefig("image.png")
plt.show()




