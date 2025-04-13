#-------remove ''' to run the code -----------# 
'''

import pandas as pd

# Load raw CSV file
csv_path = r"C:\Users\91982\Documents\AAFIN\project\colors.csv"
columns = ['colors', 'color-names', 'hex-value', 'R-value', 'G-value', 'B-value']
df = pd.read_csv(csv_path, names=columns, header=None)

#CLEANING OF CSV FILE

# Remove whitespace from string columns
df['colors'] = df['colors'].str.strip()
df['color-names'] = df['color-names'].str.strip()
df['hex-value'] = df['hex-value'].str.strip()

# Ensure RGB columns are numeric and within 0-255
for col in ['R-value', 'G-value', 'B-value']:
    df[col] = pd.to_numeric(df[col], errors='coerce')  # Convert to numeric, set invalid to NaN
    df[col] = df[col].clip(0, 255)                     # Clip values to valid RGB range

# Drop any rows with missing RGB values or color name
df.dropna(subset=['R-value', 'G-value', 'B-value', 'color-names'], inplace=True)

# Reset index after cleaning (optional)
df.reset_index(drop=True, inplace=True)

#SAVE CLEANED CSV 
cleaned_path = r"C:\Users\91982\Documents\AAFIN\project\colors_cleaned.csv"
df.to_csv(cleaned_path, index=False, header=None)

print("colors.csv preprocessed and saved as 'colors_cleaned.csv'")
