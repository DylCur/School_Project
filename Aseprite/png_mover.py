import os
import shutil

source_folder = "C://Users//dylan_ujugo02//Desktop//Aseprite//ASEPRITE"
destination_folder = "C://Users//dylan_ujugo02//Desktop//Aseprite//PNG"

# Ensure the source and destination folders exist
if not os.path.exists(source_folder) or not os.path.exists(destination_folder):
    print("Source or destination folder does not exist.")
    exit()

# Get a list of all files in the source folder
files = os.listdir(source_folder)

# Iterate over the files and move the .png files to the destination folder
for file in files:
    if file.endswith(".png"):
        source_file = os.path.join(source_folder, file)
        destination_file = os.path.join(destination_folder, file)
        shutil.move(source_file, destination_file)
        print(f"Moved {file} to {destination_folder}")
