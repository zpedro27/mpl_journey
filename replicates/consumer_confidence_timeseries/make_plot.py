import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import geopandas as gpd
from pypalettes import load_cmap
from drawarrow import ax_arrow
from highlight_text import ax_text


df = pd.read_csv("../../data/economic/economic.csv")

colors = load_cmap("Antique").colors
background_color = "#f2f2f2"

f, ax = plt.subplots(3, 3, layout="tight")
f.set_facecolor(background_color)
ax = ax.reshape(-1)

for i, (country, dfg) in enumerate(df.groupby("country")):
  ax[i].plot(dfg["date"],
             dfg["consumer confidence"],
             color=colors[i],
            )
  sns.lineplot(data=df, x="date",
               y="consumer confidence",
               estimator=None,
               units="country",
               color="lightgray", alpha=0.3,
               label=False, legend=False,
               ax=ax[i])

  # Label
  ax[i].text(dfg["date"].iloc[-1], 120, country.title(),
             color=colors[i], weight="bold",
             fontsize=10, ha="right")
  
  # Additional settings
  ax[i].set_facecolor(background_color)
  ax[i].grid(axis="y", color="lightgray", linestyle=":")
  ax[i].spines[["right", "top", "bottom"]].set_visible(False)
  ax[i].set_ylim([-60, 130])
  
  ax[i].tick_params("both", length=0, labelsize="x-small")
  ax[i].set_ylabel("")
  ax[i].set_xlabel("")
  ax[i].set_xticks(ticks=["2020-01-01", "2022-01-01", "2024-01-01"],
                  labels=["2020", "2022", "2024"])

plt.savefig("image.png")
plt.show()




