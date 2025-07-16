import os


os.system("clear")

for foldername, subfolders, filenames in os.walk("/Users/shawnconboy/Desktop/example"):
    print(f"The current folder is {foldername}")
    for subfolder in subfolders:
        print(f"\tThe current subfolder is /{subfolder}")
        for filename in filenames:
            print(f"\t\tThe current file is /{filename}")