import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from pypalettes import load_cmap
import seaborn as sns
from drawarrow import ax_arrow
from highlight_text import ax_text

world = gpd.read_file("../../data/world/world.geojson")
world = world[world["name"] != "Antarctica"]
world["continent"] = world["continent"].replace("North America", "America")
world["continent"] = world["continent"].replace("South America", "America")

df = pd.read_csv("../../data/CO2/CO2.csv")

world = world.merge(
  df,
  left_on="code_adm",
  right_on="ISO",
)
world["centroid"] = world["geometry"].centroid
x = world["centroid"].x
y = world["centroid"].y
s = world["Total"]

# Define palette:
cmap = load_cmap("Antique", cmap_type="continuous", reverse=False)
colors = {continent: cmap.colors[i] for i, continent in enumerate(world.continent.unique())}
bkg_color = "lightgray"

order_conts = world.groupby("continent")["Total"].median().sort_values(ascending=True).index

fig, ax = plt.subplots(layout="tight")
fig.set_facecolor(bkg_color)
ax.set_facecolor(bkg_color)
axins = ax.inset_axes([0.05, 0.05, 0.18, 0.6])
axins.patch.set_alpha(0)


# Display map:
for i, (g, df_cont) in enumerate(world.groupby("continent")):
  df_cont.plot(ax=ax, color=colors[g], alpha=0.6)

# Bar plot with averages per continent:
sns.boxplot(data=world, 
            y="continent", x="Total",
            ax=axins,
            order=order_conts,
            fill=False,
            fliersize=2,
              # inner="quart",
            linewidth=1,
            palette=colors,
            orient="h")
axins.spines[:].set(color="grey")
axins.spines[["top", "right"]].set_visible(False)
axins.set_yticks([])
axins.set_ylabel("")
axins.set_xlabel("")
axins.tick_params("both", length=0, labelsize=4, labelcolor="grey")
axins.text(0.98, 0.02, s="CO2 emissions/capita",
           color="grey",
           transform=axins.transAxes,
           ha="right", fontsize=4)

# Label boxplot:
for i, cont in enumerate(order_conts):
  max_val = world.loc[world.continent==cont, "Total"].max()
  axins.text(x=max_val+2,
             y=i,
             s=cont,
             color=colors[cont],
             fontsize=6,
             ha="left", va="center")


# Add bubbles:
ax.scatter(x, y, s=s*2, color="brown", alpha=0.3)

# Highlights:
# !. Arabic coutrnies:
ax_text(x=55, y=2,
	    s="<Gulf countries> \nhave the highest\nemissions.",
        ax=ax, size=4, color="grey",
	    highlight_textprops=[
	    {"color": colors["Asia"], "weight": "bold"},
	  ],
)
ax_arrow(
   tail_position=[58, 5],
   head_position=[55, 18],
   head_width=1,
   head_length=1,
   color="grey",alpha=0.3,
   radius=0.3,
   ax=ax,
)


# 2. Africa:
ax_text(x=-35, y=-15,
	    s="<Africa> is the continent\nwith the lowest\naverage emissions.",
        ax=ax, size=4, color="grey",
	    highlight_textprops=[
	    {"color": colors["Africa"], "weight": "bold"},
	  ],
)

ax_arrow(
   tail_position=[-20, -12],
   head_position=[-10, 5],
   head_width=1,
   head_length=1,
   color="grey",alpha=0.3,
   radius=-0.1,
   ax=ax,
)

# 3. Europe
ax_text(x=-60, y=35,
	    s="<Europe> is the continent\nwith the highest\naverage emissions.",
        ax=ax, size=4, color="grey",
	    highlight_textprops=[
	    {"color": colors["Europe"], "weight": "bold"},
	  ],
)

ax_arrow(
   tail_position=[-35, 38],
   head_position=[-15, 50],
   head_width=1,
   head_length=1,
   color="grey",alpha=0.3,
   radius=-0.3,
   ax=ax,
)

# Additional settings:
fig.text(0.5, 0.80,
         "CO2 emissions per capita are\nunequal around the world.",
         fontsize=15,
         ha="center")
ax.axis("off")

plt.savefig("image.png")
plt.show()




