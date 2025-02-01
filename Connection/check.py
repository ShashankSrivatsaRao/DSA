# Check for the connection to the data folder and list the files in it
import os

data_file_folder = os.path.join(os.getcwd(), 'data')
data_files = os.listdir(data_file_folder)
print(data_files)