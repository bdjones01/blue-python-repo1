import os

def extract_files_and_sizes(directory):
    file_list = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            file_size = os.path.getsize(filepath)
            file_info = {
                'name': filename,
                'size': file_size
            }
            file_list.append(file_info)
    return file_list

# Specify the directory path
directory_path = '/home/ec2-user/environment'

# Call the function to extract files and sizes
files_and_sizes = extract_files_and_sizes(directory_path)

# Print the file information
for file_info in files_and_sizes:
    print(file_info)

