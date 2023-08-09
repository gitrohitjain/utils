import os
import shutil
from sklearn.model_selection import train_test_split

def split_images(source_dir, train_dir, val_dir, test_size=0.05, random_state=42):
    # Create directories for training and validation data
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)
    
    # Get the list of image files
    image_files = os.listdir(source_dir)
    
    # Split the image files into training and validation sets
    train_files, val_files = train_test_split(image_files, test_size=test_size, random_state=random_state)
    
    # Move training images to the training directory
    for file_name in train_files:
        source_path = os.path.join(source_dir, file_name)
        target_path = os.path.join(train_dir, file_name)
        shutil.copyfile(source_path, target_path)
    
    # Move validation images to the validation directory
    for file_name in val_files:
        source_path = os.path.join(source_dir, file_name)
        target_path = os.path.join(val_dir, file_name)
        shutil.copyfile(source_path, target_path)

for what in ['images','masks']:
    source_directory = f'data/{what}'
    train_directory = f'final_data/train/{what}'
    val_directory = f'final_data/validation/{what}'
    
    split_images(source_directory, train_directory, val_directory)


