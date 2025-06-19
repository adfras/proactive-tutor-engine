

import zipfile
import os

def main():
    """
    Extracts the required datasets from the manually downloaded ZIP file.
    """
    # --- Configuration ---
    raw_data_dir = './data/raw/'
    zip_file_path = os.path.join(raw_data_dir, 'Hint_Inference_Project_Data.zip')
    
    # --- Check if the file exists ---
    if not os.path.exists(zip_file_path):
        print("="*60)
        print("ERROR: File not found!")
        print(f"Please manually download 'Hint_Inference_Project_Data.zip'")
        print(f"and place it inside the '{raw_data_dir}' folder.")
        print("Download Link: https://drive.google.com/uc?id=1SM46Ws1bw1K6mgkvqjx_rvB3d6OvF-yb")
        print("="*60)
        return

    # --- Unzip the Data ---
    print(f"Found dataset at '{zip_file_path}'.")
    print(f"Extracting data to '{raw_data_dir}'...")
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(raw_data_dir)
    
    print("\nExtraction complete.")
    print(f"Raw data is now available in the '{raw_data_dir}' directory.")

if __name__ == '__main__':
    main()