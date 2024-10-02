import os
import shutil

def copy_directory(source, destination):
    # Create destination directory if it doesn't exist
    # First, check if the destination directory exists
    
    if os.path.exists(destination):
        # If it does, remove it and all its contents
        shutil.rmtree(destination)
    
    # Now create the (empty) destination directory
    os.makedirs(destination)
    
    
    # List all items in the source directory
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)
        
        if os.path.isfile(source_path):
            # Copy file
            # Hint: use shutil.copy2 here
            shutil.copy2(source_path , dest_path)
            
        elif os.path.isdir(source_path):
            # Recursively copy directory
            # Hint: call copy_directory here
            copy_directory(source_path , dest_path)
            
        print(f"Moving {source_path }\n To {dest_path}\n")

# Don't forget to call your function in main!