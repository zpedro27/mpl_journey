import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import geopandas as gpd
from pypalettes import load_cmap
from drawarrow import ax_arrow
from highlight_text import ax_text

df = pd.read_csv("../../data/iris/iris.csv")

scheme = """
BB.
AAC
AAC
"""

fig, axs = plt.subplot_mosaic(scheme)
fig.subplots_adjust(wspace=0, hspace=0)
fig.set_facecolor("#f1f1f1")
for ax in axs:
  axs[ax].set_facecolor("#f1f1f1")
  #axs[ax].axis("off")

axs["B"].hist(df["sepal_length"], color="darkred", edgecolor="black")
axs["B"].axis("off")

axs["C"].hist(df["sepal_width"], color="purple", edgecolor="black", orientation="horizontal")
axs["C"].axis("off")

axs["A"].scatter(df["sepal_length"], df["sepal_width"], color="black")
axs["A"].text(0.95, 0.95, "Sepal length",
              weight="bold", color="darkred",
              ha="right",
              transform=axs["A"].transAxes)
axs["A"].text(0.95, 0.05, "Sepal width",
              weight="bold", color="purple",
              rotation=-90,
              transform=axs["A"].transAxes)

axs["A"].spines[["left", "bottom"]].set_visible(False)
axs["A"].set_xticks([])
axs["A"].set_yticks([])

plt.savefig("image.png")
plt.show()




