import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import geopandas as gpd
from pypalettes import load_cmap
from drawarrow import ax_arrow
from highlight_text import ax_text

from PIL import Image
import numpy as np

# Load iamge
image = Image.open("../../data/misc/cat.png")
img = np.asarray(image)

fig, ax = plt.subplots(1, 2, figsize=(10,5), layout="tight")
fig.subplots_adjust(wspace=0)

# Small image
axins = ax[0].inset_axes([0.4, 0.4, 0.2, 0.2])
axins.imshow(img)
axins.axis("off")

# Add lines
ax[0].plot([0.6, 1], [0.6, 0.9], c="black")
ax[0].plot([0.6, 1], [0.4, 0.1], c="black")
ax[0].set_xlim([0, 1])
ax[0].set_ylim([0, 1])

# Zoomed image
ax[1].imshow(img)

for ax_ in ax:
  ax_.axis("off")


plt.savefig("image.png")
plt.show()




