import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load image
img_path = r"C:\Users\91982\Documents\AAFIN\project\pic2.jpg"
# visualization of second pic remove # from it and add to the above line
#img_path = r"C:\Users\91982\Documents\AAFIN\project\pic2.jpg"
img = cv2.imread(img_path)
if img is None:
    raise FileNotFoundError("Image not found, Check the image path.")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Load color CSV file data
csv_path = r"C:\Users\91982\Documents\AAFIN\project\colors_cleaned.csv"
cols = ['colors', 'color-names', 'hex-value', 'R-value', 'G-value', 'B-value']
df = pd.read_csv(csv_path, names=cols, header=None)


# Image data for clustering
pixels = img_rgb.reshape((-1, 3))

# KMeans to find dominant colors - Set to 7 clusters
kmeans = KMeans(n_clusters=7, random_state=0)
kmeans.fit(pixels)
colors = kmeans.cluster_centers_.astype(int)
counts = np.bincount(kmeans.labels_)

# Function to get closest color name from CSV
def get_color_name(R, G, B):
    min_dist = float('inf')
    name = "Unknown"
    for _, row in df.iterrows():
        dist = abs(R - row['R-value']) + abs(G - row['G-value']) + abs(B - row['B-value'])
        if dist < min_dist:
            min_dist = dist
            name = row['color-names']
    return name

# Disable toolbar
plt.rcParams['toolbar'] = 'None'

# labels for the pie chart with color names and RGB values
labels = []
hex_colors = []
for color in colors:
    r, g, b = color
    name = get_color_name(r, g, b)
    labels.append(f"{name} ({r}, {g}, {b})")
    hex_colors.append(f'#{r:02x}{g:02x}{b:02x}')

# Sort by frequency of colors
sorted_idx = np.argsort(counts)[::-1]
labels = [labels[i] for i in sorted_idx]
hex_colors = [hex_colors[i] for i in sorted_idx]
counts = counts[sorted_idx]

# plot original image and pie chart
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Display image with pie chart
axs[0].imshow(img_rgb)
axs[0].axis('off')  # Hide axes
axs[0].set_title("Original Image")

# Pie chart for dominant colors
axs[1].pie(counts, labels=labels, colors=hex_colors, autopct='%1.1f%%', startangle=90)
axs[1].set_title("Dominant Colors")

# layout for display
plt.tight_layout()
plt.show()

''' pic1 image referance 
https://images.app.goo.gl/93n7ZfMWvne5mMrk6
https://www.istockphoto.com/photo/beautiful-flowers-background-gm520700958-91057065
pic2 made using paint app by Aafin 
'''