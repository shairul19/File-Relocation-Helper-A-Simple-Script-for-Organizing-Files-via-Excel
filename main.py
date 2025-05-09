import os
import shutil
import pandas as pd

# Path to the Excel file and source/destination folders
excel_path = './file_list.xlsx'  # Path to your Excel file
source_folder = './source_data'  # Path to the folder containing the PDF files
destination_folder = './archive'  # Path to the folder where PDF files will be moved

# Read data from the Excel file
df = pd.read_excel(excel_path)
file_list = df['file_Name'].tolist()  # Adjust to match the column header in the Excel file

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Move files
for file_name in file_list:
    file_path = os.path.join(source_folder, file_name)
    if os.path.exists(file_path):
        shutil.move(file_path, destination_folder)
        print(f"File {file_name} was successfully moved.")
    else:
        print(f"File {file_name} was not found in the source folder.")
