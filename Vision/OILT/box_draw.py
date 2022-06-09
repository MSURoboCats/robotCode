import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

im = Image.open('Gate1frame271_img.jpg')

# Create figure and axes
fig, ax = plt.subplots()

# Display the image
ax.imshow(im)

# Create a Rectangle patch
rect1 = patches.Rectangle((156, 211), 264, 155, linewidth=1, edgecolor='r', facecolor='none')
#rect2 = patches.Rectangle((211, 131), 98, 177, linewidth=1, edgecolor='r', facecolor='none')

# Add the patch to the Axes
ax.add_patch(rect1)
#ax.add_patch(rect2)

plt.show()
