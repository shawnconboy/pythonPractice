import os, sys, time, shutil

# rename files without location code
# save renamed files in a new folder
# right? is that all? simple project...

# RT - Router, SW - Switch, FW - Firewall
# SO_01_125_001 (southern shops_building01_room12_deviceNumber001)

# so we should be going from 
# FW_GR_01_100-002.cfg to GRN_FW_GR_01_100-002.cfg

# GRN for greenville

# clears screen.
os.system("clear")

# takes input from user to be added to names
locationCode = input("Please enter location code to be added (GSP, CLT, TNN) : ")

# assigns paths to variables accordingly
configFolder = ("/Users/shawnconboy/Desktop/Configuration Files")
newFolder = ("/Users/shawnconboy/Desktop/NewConfigs")

# if the "new folder" variable's path doesn't
# exist, make the folder for that path to be true
if not os.path.exists(newFolder):
    os.makedirs(newFolder)

# loops through the files in "config folder"
for configFile in os.listdir(configFolder):

    # find all files ending in ".cfg"
    if configFile.endswith(".cfg"):

        # add the location code to them thangs
        # by renaming with the code appended
        addLocationCode = f"{locationCode}_{configFile}"

        # take oldPath and newPath to copy newly named file to "newPath"
        oldPath = os.path.join(configFolder, configFile)
        newPath = os.path.join(newFolder, addLocationCode)
        shutil.copy(oldPath, newPath)
print("\nProgram ended. New files have been moved and copied.")

# this program was tedious.  I used chatGPT to try
# and help break down and explain a lot.
# i think the book's explanations using windows
# paths and my mac's native paths are clashing
# and making things a bit more difficult for me.