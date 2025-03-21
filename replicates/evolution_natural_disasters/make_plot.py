import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import geopandas as gpd
from pypalettes import load_cmap
from drawarrow import ax_arrow
from highlight_text import ax_text
import numpy as np

df = pd.read_csv("../../data/natural-disasters/natural-disasters.csv")

columns = df.drop(columns="Year").sum().sort_values().index.to_list()
x = df["Year"]
y = np.stack(df[columns].values, axis=-1)

fig, ax = plt.subplots(figsize=(10, 5))

# Here goes your code
cmap = load_cmap("Antique")
ax.stackplot(x, y, colors=cmap.colors, labels=columns)

ax.text(0.02, 0.9, "Evolution of natural disasters\nbetween 1960 and 2023",
       transform=ax.transAxes, fontsize=22)
ax.text(0.02, 0.85, "Data source: EM-DAT",
       transform=ax.transAxes, )

ax.yaxis.tick_right()
ax.spines[["top", "left"]].set_visible(False)
ax.set_xlim([1960, x.max()])


xticks = 1960 + 10*np.arange(start=0, stop=7, step=2)
ax.set_xticks(ticks=xticks, labels=[int(c) for c in xticks])
ax.tick_params("both", length=0)

h, l = ax.get_legend_handles_labels()
ax.legend(handles=h[::-1], labels=l[::-1], loc="center left", fontsize=10)

plt.savefig("image.png")
plt.show()




