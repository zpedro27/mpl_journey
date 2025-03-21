import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import geopandas as gpd
from pypalettes import load_cmap
from drawarrow import ax_arrow
from highlight_text import ax_text


world = gpd.read_file("../../data/world/world.geojson")
df = pd.read_csv("../../data/CO2/CO2.csv")

world = world.merge(df, left_on="code_adm", right_on="ISO")
europe = world[world["continent"] == "Europe"]
europe = europe[europe["name"] != "Russia"]

cmap = load_cmap("Sunset2", cmap_type="continuous")

fig, ax = plt.subplots(layout="tight")
europe.plot(
  column="Total",
  cmap=cmap,
  edgecolor="black",
  linewidth=0.4,
  legend=True,
  legend_kwds={"shrink": 0.5},
  ax=ax
)

ax.set_xlim(-25, 41)
ax.set_ylim(33, 82)
ax.axis("off")

ax_arrow(
  [0, 65], [5.5, 50],
  color="black",
  radius=0.2,
  fill_head=False
)
ax.text(x=-5, y=66, s="Luxembourg")

ax.text(
  x=-25, y=73,
  s="CO2/Capita in Europe in 2021",
  size=16
)

plt.savefig("image.png")
plt.show()




