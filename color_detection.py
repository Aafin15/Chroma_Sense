import cv2
import pandas as pd
import numpy as np

# Path of image
img_path = r"C:\Users\91982\Documents\AAFIN\project\pic1.jpg"
# for using second sample pic  --- pic2 
# img_path = r"C:\Users\91982\Documents\AAFIN\project\pic2.jpg" 

# Path of colors_cleaned.csv file (preproceeced)
colors_csv_path = r"C:\Users\91982\Documents\AAFIN\project\colors_cleaned.csv"

# Column names for CSV file
index = ['colors', 'color-names', 'hex-value', 'R-value', 'G-value', 'B-value']

img = cv2.imread(img_path)

# Check if the image loaded properly
if img is None:
    print("Error: Image could not be loaded, Please check the path.")
    exit()

# read CSV file
try:
    df = pd.read_csv(colors_csv_path, names=index, header=None)
except FileNotFoundError:
    print("Error: colors.csv file not found. Please check the path.")
    exit()

# global variables 

clicked = False
r = g = b = xpos = ypos = 0

# function to get color name based on RGB values from csv

def getColorName(R, G, B):
    minimum = 10000
    colorName = "Unknown"

    for i in range(len(df)):
        d = abs(R - int(df.loc[i, 'R-value'])) + abs(G - int(df.loc[i, 'G-value'])) + abs(B - int(df.loc[i, 'B-value']))
        if d <= minimum:
            minimum = d
            colorName = df.loc[i, "color-names"]
    return colorName

# function to handle mouse click event(double)

def selectColor(event, x, y, flags, param):
    global b, g, r, xpos, ypos, clicked
    if event == cv2.EVENT_LBUTTONDBLCLK:
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

#  window setup

cv2.namedWindow('image')  
cv2.setMouseCallback('image', selectColor)  

# Now show the image
cv2.imshow('image', img)  

# Last selected values
last_r = last_g = last_b = 0
last_color_name = ""
selected = False

# Last selected values
last_r = last_g = last_b = 0
last_color_name = ""
selected = False
 
def draw_text_with_background(
    image, text, pos, font, font_scale, text_color, thickness=1, bg_opacity=0.4):
    # Get size of the text
    (text_w, text_h), baseline = cv2.getTextSize(text, font, font_scale, thickness)
    x, y = pos

    # Creating background 
    bg_x1, bg_y1 = x - 5, y - text_h - 5
    bg_x2, bg_y2 = x + text_w + 5, y + 5

    # Clip to image bounds
    bg_x1 = max(bg_x1, 0)
    bg_y1 = max(bg_y1, 0)

    # background
    overlay = image.copy()
    cv2.rectangle(overlay, (bg_x1, bg_y1), (bg_x2, bg_y2), (0, 0, 0), -1)
    cv2.addWeighted(overlay, bg_opacity, image, 1 - bg_opacity, 0, image)

    # Draw the text
    cv2.putText(image, text, (x, y), font, font_scale, text_color, thickness, cv2.LINE_AA)

while True:
    display_img = img.copy()

    if selected:
        # Swatch settings
        swatch_x, swatch_y = 20, 20
        swatch_w, swatch_h = 120, 40

        # Color swatch
        cv2.rectangle(display_img, (swatch_x, swatch_y),
                      (swatch_x + swatch_w, swatch_y + swatch_h),
                      (last_b, last_g, last_r), -1)

        # Border
        cv2.rectangle(display_img, (swatch_x, swatch_y),
                      (swatch_x + swatch_w, swatch_y + swatch_h),
                      (60, 60, 60), 1)

        # Auto change of font color for readability
        brightness = last_r * 0.299 + last_g * 0.587 + last_b * 0.114
        text_color = (0, 0, 0) if brightness > 160 else (255, 255, 255)

        # text
        color_text = f"{last_color_name.upper()}  R:{last_r} G:{last_g} B:{last_b}"
        font = cv2.FONT_HERSHEY_DUPLEX
        font_scale = 0.6
        thickness = 1

        # Position
        text_x = swatch_x + swatch_w + 15
        text_y = swatch_y + 28

        # text with background
        draw_text_with_background(display_img, color_text, (text_x, text_y), font, font_scale, text_color, thickness, bg_opacity=0.4)

    # Display the image
    cv2.imshow('image', display_img)

    # Update on click
    if clicked:
        last_r, last_g, last_b = r, g, b
        last_color_name = getColorName(r, g, b)
        selected = True
        clicked = False

    # Exit on ESC
    if cv2.waitKey(20) & 0xFF == 27:
        break

    # Press ESC key or close window to exit
    key = cv2.waitKey(1)
    if key == 27 or cv2.getWindowProperty('image', cv2.WND_PROP_VISIBLE) < 1:
        break

cv2.destroyAllWindows()

