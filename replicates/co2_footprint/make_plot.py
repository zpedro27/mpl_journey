import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import geopandas as gpd
from pypalettes import load_cmap
from drawarrow import ax_arrow
from highlight_text import ax_text
import numpy as np

footprint = pd.read_csv("../../data/footprint/footprint.csv")

x = footprint["gdpCapita"]
y = footprint["footprint"]
s = footprint["populationMillions"]

background_color = "#252647"
white = "#f1f1f1"
light_grey = "#bab9b9"

fig, ax = plt.subplots()
ax.scatter(
  x, y, s=s*1.4,
  alpha=0.8, color="darkred",
  edgecolor=white, linewidth=0.5
)

fig.set_facecolor(background_color)
ax.set_facecolor(background_color)

ax.spines[["top", "right"]].set_visible(False)
ax.spines[["left", "bottom"]].set_color(light_grey)

ax.tick_params(length=0, color=light_grey)

ticks = np.linspace(start=1, stop=4, num=4)
ax.set_xticks(20000*ticks, labels=[f"${int(20*x)}k" for x in ticks], color=light_grey)

ticks = np.linspace(start=0, stop=12, num=4)
ax.set_yticks(ticks, [ int(x) for x in ticks], color=light_grey)

ax.set_xlim([-1000, 85000])
ax.set_ylim([0, 12.5])


df_sel = footprint.loc[footprint.populationMillions > 100]
for i, row in df_sel.iterrows():
  ax.text(x=row["gdpCapita"], 
          y=row["footprint"],
          s=row["country"],
          color="white", fontsize=9,
         horizontalalignment="center")

ax.text(2000, 10.5, "More capita, more footprint", fontsize=20, color=white)
ax.text(1000, 12, "Global hectares per person", fontsize=8, color=light_grey)
ax.text(70000, 0.5, "GDP per capita", fontsize=8, color=light_grey)

plt.savefig("image.png")
plt.show()




