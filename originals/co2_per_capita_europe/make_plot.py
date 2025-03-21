import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from pypalettes import load_cmap
import seaborn as sns
from drawarrow import ax_arrow
from highlight_text import ax_text

world = gpd.read_file("../../data/world/world.geojson")
df = pd.read_csv("../../data/co2/co2.csv")

# Colors:
bkg_color = "white"
cmap = load_cmap("Alosa_fallax", reverse=False, cmap_type="continuous")


# Data preparation:
world = world.merge(df, left_on="code_adm", right_on="ISO")
europe = world.loc[(world.continent == "Europe") & (world.name != "Iceland")]

emissions = ["Coal", "Gas", "Oil", "Cement", "Flaring", "Other"]

df_means = europe[emissions].mean().T.sort_values(ascending=False).reset_index().rename(columns={"index": "emission_type", 0: "mean"})
df_pt = europe.loc[europe.name=="Portugal"][emissions].T.reset_index().rename(columns={"index": "emission_type", 158: "mean"})


# Define image:
fig, ax = plt.subplots(layout="tight")
fig.set_facecolor(bkg_color)
ax.set_facecolor(bkg_color)

LONG_MIN = -20
LONG_MAX = 45
LAT_MIN = 30
LAT_MAX = 75
ax.set_ylim([LAT_MIN, LAT_MAX])
ax.set_xlim([LONG_MIN, LONG_MAX])
ax.axis("off")

# Display europe
europe.plot(column="Total", edgecolor="black", cmap=cmap, linewidth=0.5, ax=ax, legend=False)

# Highlight PT:
europe.loc[europe.name=="Portugal"].boundary.plot(alpha=0.3, edgecolor="black", linewidth=4, ax=ax)

# Inset:
axins=ax.inset_axes([0.05, 0.65, 0.2, 0.3])
sns.barplot(data=df_means, y="emission_type", x="mean", 
            edgecolor="black", facecolor="white", 
            linestyle="--", linewidth=0.5,
            ax=axins, orient="h")

sns.barplot(data=df_pt, y="emission_type", x="mean", 
            color=cmap.colors[-1], #"lightgray",
            alpha=0.6,
            ax=axins, orient="h")

# add labels:
for i, (_, row) in enumerate(df_means.iterrows()):
  axins.text(row["mean"]+0.12, i, row["emission_type"],
             ha="left", va="center",
             color="gray", fontsize="x-small")

# additional settings:
axins.patch.set_alpha(0)
axins.spines[["right", "bottom"]].set_visible(False)
axins.spines[["left", "top"]].set(color="gray")
axins.xaxis.set_ticks_position("top")
axins.set_yticks([], [])
axins.set_ylabel("", fontsize="xx-small")
axins.set_title("CO2 emissions per capita", fontsize="xx-small", color="grey")
axins.set_xlabel("")
axins.tick_params("both", length=0, labelsize=6, labelcolor="gray", pad=0)
#axins.text(0.8, 1., "CO2 emissions", transform=axins.transAxes)

# Add main title:
ax_text(x=LONG_MIN + 5, y=LAT_MIN + 4,
	    s="<Portugal> lower CO2 emissions per capita\nthan the average european country.",
        ax=ax, size=12,
	    highlight_textprops=[
	    {"color": "grey", "weight": "bold"},
	  ],
)

# Add Legend on main plot:
value_ranges = [0, 4, 8, 12, 16]
labels = ["0-4", "4-8", "8-12", "12-16"]


text_params = {"fontsize": "x-small",
               "color": "grey",
               "ha": "right", 
               "va": "center"}
for i in range(len(value_ranges) - 1):
  vmin = value_ranges[i]
  vmax = value_ranges[i+1]
  vmean = (vmax + vmin)/2
  vmean /= (value_ranges[-1] - value_ranges[0])
  color = cmap(vmean)

  ax.add_patch(
    plt.Rectangle(
      (LONG_MAX-5, LAT_MIN + 2.5*i),
      2,
      2,
	  facecolor=color,
	  edgecolor="black",
	  lw=0.6,
      clip_on=False,
	  )
    )

  ax.text(LONG_MAX-5.5, LAT_MIN+1 + 2.5*i,
          labels[i], **text_params)

## Legend title:
ax.text(LONG_MAX, LAT_MIN + 3.7*i,
        "Total CO2\nemissions per capita", **text_params)

# Add arrow:	
ax_arrow(
   tail_position=[-9, 42],
   head_position=[-14, 58],
   color="lightgray",
   fill_head=True,
   radius=-0.2,
   ax=ax,
)

plt.savefig("image.png")
plt.show()




