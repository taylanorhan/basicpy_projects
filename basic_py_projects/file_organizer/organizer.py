import os
import shutil

def organize_files(source_dir):
    for file_name in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir, file_name)):
            # Get the file extension
            extension = os.path.splitext(file_name)[1][1:].lower()

            # Define destination directories based on file types
            destination_folder = None
            if extension in ['jpg', 'png', 'gif']:
                destination_folder = 'Images'
            elif extension in ['doc', 'pdf', 'txt']:
                destination_folder = 'Documents'
            # Add more conditions for different file types

            if destination_folder:
                destination_path = os.path.join(source_dir, destination_folder)
                os.makedirs(destination_path, exist_ok=True)
                shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_path, file_name))


