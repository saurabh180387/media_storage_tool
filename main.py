import os

all_files = list()
all_dirs = list()


if __name__ == "__main__":
    x=input("Please provide the path location of the media files and doc files ")
    try:
        if os.path.exists(x):
            pass
        my_path=os.path.isdir()
    except:
        raise FileNotFoundError(e)

