import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import geopandas as gpd
from pypalettes import load_cmap
from drawarrow import ax_arrow
from highlight_text import ax_text

# Load data:
df = pd.read_csv("../../data/wine/wine.csv")
df_agg = df.groupby("quality", as_index=False).median()


fig, ax = plt.subplots(layout="tight")

cmap = load_cmap("RdYlGn", cmap_type="continuous", reverse=False)
n_scales = len(df_agg)

# Display bars:
ax.barh(
  df_agg["quality"],
  df_agg["residual_sugar"],
  color=[cmap(i/n_scales) for i in range(n_scales)],
  edgecolor="lightgray"
)

# Add residual sugar as label
for i, row in df_agg.iterrows():
  ax.text(row["residual_sugar"]-0.2,
          row["quality"],
          f"{row['residual_sugar'] :.1f}",
          horizontalalignment="right",
          verticalalignment="center",
          color="black",
         )

# Change xy labels
ax.set_xlabel("Residual Sugar\n(remaining after fermentation)",
              color="grey",
              fontsize=8)

ax.set_ylabel("Quality",
              color="grey",
              fontsize=8)

# Main title
ax.text(
  y=5.5,
  x=15,
  s="Both good and bad wines\nhave high residual sugar",
  size=15,
  ha="left", va="center",
)

# Extra config
ax.spines[["right", "top", "bottom", "left"]].set_visible(False)
ax.tick_params("both", length=0)
ax.set_xticks([], [])

ax.set_yticks(ticks=df_agg["quality"], labels=df_agg["quality"],
              fontsize=8,
              color="grey")

plt.savefig("image.png")
plt.show()




