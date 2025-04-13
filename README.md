# 🎨 Chroma_Sense

**ChromaSense** is a data-driven project that uses machine learning and computer vision to detect, classify, and analyze colors from digital images. Colors play a vital role in design, marketing, image processing, fashion, and quality control. This tool extracts meaningful insights from color data to support better decisions and understanding of visual content.

---

## 📌 What It Does

- Detects **dominant colors** from any image using KMeans clustering.
- Matches detected colors with human-readable names using a custom CSV dataset.
- Visualizes results in a **pie chart** with percentage, color name, and RGB values.
- Displays the **original image** alongside the analysis for visual comparison.

---

## ⚙️ How It Works

- **Image Processing**: Loads the image and converts it from BGR to RGB using OpenCV.
- **Clustering**: Applies KMeans (from `scikit-learn`) to identify dominant colors.
- **Color Matching**: Uses `colors_cleaned.csv` to find the closest color name for each RGB value.
- **Visualization**: Generates a pie chart (via Matplotlib) showing dominant colors and their proportions.

---

## 💻 Technologies Used

- **Python**  
- **OpenCV** – Image reading and processing  
- **Pandas** – Reading and processing the CSV color dataset  
- **scikit-learn** – KMeans clustering algorithm  
- **Matplotlib** – Visualizing results with pie charts and side-by-side image comparison  

---

## 📁 Project Files

| File Name           | Description                                          |
|---------------------|------------------------------------------------------|
| `Visualization.py`  | script to run color detection and visualization      |
| `color_detection.py`| script for color detection                           |
| `colors_cleaned.csv`| Dataset with color names and RGB values              |
| `pic1.jpg`          | Sample image (can be replaced with your own)         |
| `pic2.jpg`          | Another sample image                                 |

---
📷 Example Output
![image](https://github.com/user-attachments/assets/a45a17ab-1dad-4364-9c33-375c1d81e871)

A side-by-side display of:
✅ Original Image
✅ Pie chart showing dominant colors with RGB values and color names
![image](https://github.com/user-attachments/assets/afb48fcf-76a8-4d38-896a-6931ed379468)
pic2
![image](https://github.com/user-attachments/assets/a6d8c3da-0024-4647-998c-f6a61de816dc)



----

## 🌱 Future Scope

- **Real-time color analysis from webcam/video** 
- **GUI interface using Tkinter or Dash**   
- **Support for batch image processing**

---

📌 License
This project is open-source and free to use for personal or academic projects.



### 📦 Install required libraries:

You can run these commands in your terminal or command prompt.
```bash 
pip install numpy
pip install pandas
pip install opencv-python
pip install scikit-learn
pip install matplotlib



