import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import geopandas as gpd
from pypalettes import load_cmap
from drawarrow import ax_arrow
from highlight_text import ax_text

df = pd.read_csv("../../data/economic/economic.csv")

fig, axs = plt.subplots(
    ncols=3, nrows=3, layout="tight"
)

for country, ax in zip(df["country"].unique(), axs.flat):
    x = df.loc[df["country"] == country, "consumer confidence"]
    sns.kdeplot(x, ax=ax, color="purple", fill=True)
    ax.text(0.01, 0.9, f"consumer confidence in\n{country}",
            fontsize=7,
            transform=ax.transAxes)
    ax.set_xlim([-60, 130])
    ax.set_ylim([0, 0.1])
    ax.spines[["top", "left", "right"]].set_visible(False)
    ax.tick_params("both", length=0)
    ax.set_yticks([])
    ax.set_ylabel("")
    ax.set_xlabel("")

plt.savefig("image.png")
plt.show()




