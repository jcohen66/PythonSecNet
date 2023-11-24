import os
file_count = 0
for currentdir, dirnames, filenames in os.walk("."):
    file_count += len(filenames)
print(f"Total number of files {file_count}")
