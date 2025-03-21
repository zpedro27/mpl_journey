import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import geopandas as gpd
from pypalettes import load_cmap
from drawarrow import ax_arrow
from highlight_text import ax_text

# Read data:
df = pd.read_csv("../../data/economic/economic.csv")

# Data cleanup:
df = df.replace({"united kingdom": "uk",
                 "united states": "us"})
df = df.loc[df["country"].isin(["uk", "us", "canada",
                                "australia", "china",
                                "switzerland", "japan"])]

# Define palette
bkg_color = "#191c3b"
colors = {"china": "#d84d4f", 
          "switzerland": "#49ca80",
          "japan": "#d65ce7",
          "australia": "#786dea",
}

# Define figure:
fig, ax = plt.subplots(2, 2, 
                       sharey=True,
                       figsize=(9,9),
                       #layout="tight"
                      )
fig.set_facecolor(bkg_color)
ax=ax.reshape(-1)

# Add title:
fig.subplots_adjust(top=0.9)
fig.text(0.12, 0.95,  "Interest rates, from 2020 to 2024", color="lightgray", fontsize=20)

# Display lines:
for i, (country, col) in enumerate(colors.items()):
  ax[i].set_facecolor(bkg_color)

  df_others = df.loc[df.country != country]
  for g, dfg in df_others.groupby("country"):
    ax[i].plot(dfg["date"], dfg["interest rates"], c="gray")
    ax[i].text(dfg["date"].iloc[-1], 
               dfg["interest rates"].iloc[-1], 
               g.upper(), color="gray", fontsize=8,)
  
  dfg = df.loc[df.country==country]  
  ax[i].plot(dfg["date"], dfg["interest rates"], color=col,)
  ax[i].text(dfg["date"].iloc[-1],
             dfg["interest rates"].iloc[-1], 
             country.upper(), color=col, fontsize=8,)

  
  ax[i].set_xticks(["2020-01-01", "2022-01-01", "2024-01-01"],
                  labels=["2020", "2022", "2024"])
  ax[i].tick_params("both", color="lightgray", labelcolor="lightgray")

  if i%2 == 1:
    ax[i].spines[["top", "right", "left"]].set_visible(False)
    ax[i].tick_params("y", length=0)
    ax[i].spines[["bottom"]].set(color="lightgray")

  else:
    ax[i].spines[["top", "right"]].set_visible(False)
    ax[i].spines[["bottom", "left"]].set(color="lightgray")


plt.savefig("image.png")
plt.show()




