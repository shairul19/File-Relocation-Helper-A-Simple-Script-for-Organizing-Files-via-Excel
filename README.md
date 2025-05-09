# File-Relocation-Helper-A-Simple-Script-for-Organizing-Files-via-Excel
This repository contains a Python script designed to automate the process of moving PDF files from a source folder to a destination folder based on a list provided in an Excel file.

## Features
- Reads PDF file names from an Excel file.
- Checks for the existence of each file in the source folder.
- Moves existing PDF files to the specified destination folder.
- Logs the success or failure of each file transfer operation.

## Requirements
To run this script, you need:

- Python 3.6 or later
- The following Python libraries:
  - `pandas`
  - `openpyxl`

You can install the required libraries using pip:
```bash
pip install pandas openpyxl

**Usage**
1. Clone this repository or download the script.
2. Ensure you have an Excel file with a column named file_Name containing the PDF file names to be moved.
3. Place the Excel file and the source folder containing PDF files in the appropriate paths.
4. Update the following variables in the script to match your setup:
- excel_path: Path to your Excel file.
- source_folder: Path to the folder containing the PDF files to be moved.
- destination_folder: Path to the folder where PDF files will be moved.

**Run the script:**
python file_transfer.py

**File Structure**
Assume the following file structure before running the script:

project_directory/
├── file_transfer.py
├── file_list.xlsx
├── source_data/   # Source folder containing PDF files
│   ├── file1.pdf
│   ├── file2.pdf
│   └── ...
├── archive/       # Destination folder (created automatically if not exists)
After running the script, the PDF files listed in file_list.xlsx will be moved from the source_data folder to the archive folder.

**Output**
The script logs messages to the console indicating the success or failure of each file transfer operation:
File [filename] was successfully moved.: File successfully moved.
File [filename] was not found in the source folder.: File not found in the source folder.
