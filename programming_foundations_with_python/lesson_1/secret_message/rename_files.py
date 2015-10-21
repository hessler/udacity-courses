import os
from string import maketrans

directory_path = "prank"

def rename_files():
    # 1. Get filenames from a folder
    files = os.listdir(directory_path)
    
    # Get current working directory
    saved_path = os.getcwd()
    print "Current Working Directory: " + saved_path
    
    # Change working directory
    os.chdir(directory_path)
    print "Changed Working Directory: " + os.getcwd()
    
    # 2. For each file, rename it by removing numbers
    for file_name in files:
        print "Old Name: " + file_name
        print "New Name: " + file_name.translate(None, "0123456789")
        
        # Without doing the working directory logic, can use these 3 lines
        #original_name = os.path.join(directory_path, file_name)
        #new_name = os.path.join(directory_path, file_name.translate(None, "0123456789"))
        #os.rename(original_name, new_name)
        
        # Single-line rename solution using working directory logic
        os.rename(file_name, file_name.translate(None, "0123456789"))

rename_files()