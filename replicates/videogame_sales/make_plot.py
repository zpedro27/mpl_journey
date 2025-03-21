import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import geopandas as gpd
from pypalettes import load_cmap
from drawarrow import ax_arrow
from highlight_text import ax_text


#Load data:
df = pd.read_csv("../../data/game-sales/game-sales.csv")

# Define colors:
colors = load_cmap("Antique").colors
col1, col2 = colors[0], colors[1]


# Clean up data:
to_remove = [" Interactive",  " Digital Entertainment", " Computer Entertainment",
             " Bandai Games",  " Entertainment",  " Game Studios"]
for rem in to_remove:
  df["Publisher"] = df["Publisher"].str.replace(rem, "")

# Calculate total sales:
df_90s = df.loc[(df.Year >= 1990)
& (df.Year <= 1999)].groupby(["Publisher"]).sum().reset_index().sort_values(by="Global_Sales", ascending=False).iloc[0:10]
df_00s = df.loc[(df.Year >= 2000) & (df.Year <= 2009)].groupby(["Publisher"]).sum().reset_index().sort_values(by="Global_Sales", ascending=False).iloc[0:10]

# Get figure:
fig, ax = plt.subplots(2, 1, figsize=(8, 10),
                       sharex=True)
fig.subplots_adjust(hspace=0)
ax = ax.reshape(-1)

# Display data:
ax[0].barh(y=df_90s["Publisher"], width=df_90s["Global_Sales"],
           color=col1)
ax[1].barh(y=df_00s["Publisher"], width=df_00s["Global_Sales"],
           color=col2)

# Display company names:
for i, (_, row) in enumerate(df_90s.iterrows()):
  ax[0].text(x=row["Global_Sales"]+10, y=i,
             s=row["Publisher"], ha="left", va="center")

for i, (_, row) in enumerate(df_00s.iterrows()):
  ax[1].text(x=10, y=i,
             s=row["Publisher"], ha="left", va="center")

# Display text:
ax_text(x=200, y=8, s="Overall sales during the <90s>", 
        ax=ax[0], fontsize=20,
        highlight_textprops=[
	    {"color": col1, "weight": "bold"},]
)

ax_text(x=200, y=8, s="Overall sales during the <2000s>", 
        ax=ax[1], fontsize=20,
        highlight_textprops=[
	    {"color": col2, "weight": "bold"},]
)

fig.text(0.5, 0.9, "Video game sales by major publishers",
         ha="center", fontsize=25)

# Additional configs:
ax[0].spines[["top", "left", "right"]].set_visible(False)
ax[1].spines[["left", "right"]].set_visible(False)
ax[1].xaxis.set_major_formatter('{x:.0f}M')
for ax_ in ax:
  ax_.tick_params("both", length=0)
  ax_.set_yticks([])
  ax_.grid("x", linestyle=":")

plt.savefig("image.png")
plt.show()




