import os

all_files = list()
all_dirs = list()

# Iterate for each dict object in os.walk()
for root, dirs, files in os.walk("root/home/project"):
	# Add the files list to the all_files list
	all_files.extend(files)
	# Add the dirs list to the all_dirs list
	all_dirs.extend(dirs)

print(all_files)
print(all_dirs)
