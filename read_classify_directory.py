import os
import global_config.py
    
gdrive_files = []
s3_files=[]

def get_file_extensions(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_extension = os.path.splitext(file)[1]
            if file_extension in gdrive_file_type:
                gdrive_files.append(file)
            elif  file_extension in  s3_file_images or file_extension in  s3_file_media :
                s3_files.append(file)
            
    #return True

global path
extensions = get_file_extensions(path)

def send_to_cloud():
    ##

    


