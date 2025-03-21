import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import geopandas as gpd
from pypalettes import load_cmap
from drawarrow import ax_arrow
from highlight_text import ax_text

df = pd.read_csv("../../data/economic/economic.csv")

params = {"united states": ("#ae2f2f", 4),
          "japan": ("#44487e", 4),
          "others": ("#b9b9b9", 1)}

# Get figure:
fig, ax = plt.subplots(figsize=(10, 5))
fig.set_facecolor("#fffaf4")
ax.set_facecolor("#fffaf4")

# Add title:
fig.subplots_adjust(top=0.85)
fig.text(x=0.5, y=0.9,
         s="Unemployment rates during COVID-19",
         fontsize=25,
         ha="center")
fig.text(x=0.5, y=0.85,
         s="From January 2020 to December 2023",
         fontsize=14,
         color="#b9b9b9",
         ha="center")

# Display data:
for country, dfg in df.groupby("country"):
  
  try:
    c, lw = params[country]
  except KeyError:
    c, lw = params["others"]
    
  plt.plot(dfg["date"],
           dfg["unemployment rate"],
           color=c, linewidth=lw)
  
# Add annotations:
ax_text(x=5, y=14,
	    s="The <USA> had a peak unemployment\nrate of <14.9%> in April 2020.",
        ax=ax, size=14,
	    highlight_textprops=[
	    {"color": params["united states"][0], "weight": "bold"},
	    {"weight": "bold"},
	  ],
)

ax_text(x=15, y=2,
	    s="<Japan> has maintained a very low unemployment\nrate during the entire period.",
        ax=ax, size=14,
	    highlight_textprops=[
	    {"color": params["japan"][0], "weight": "bold"},
	  ],
)


# Define axes:
ax.spines[["top", "left", "right", "bottom"]].set_visible(False)
ax.grid(axis="y", color="#b9b9b9", alpha=0.2)

ax.tick_params(length=0)
ax.set_xticks(ticks=[dfg["date"].min(), dfg["date"].max()],
              labels=["Jan 2020", "Dex 2023"],
              color="#b9b9b9",
              fontsize=10)
ax.set_ylim([-0.01, 15])
ax.set_yticklabels(labels=ax.get_yticklabels(), fontsize=14)

plt.savefig("image.png")
plt.show()




