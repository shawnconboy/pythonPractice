# Create a program to update the required Algebra entrance test scores for Anywhere Community College.

# The spreadsheet named Entrance Test Scores (also attached to this assignment) contains a list of academic programs in which the Algebra test scores have changed.

# Since this spreadsheet was created, academic department chairs have increased the entrance test score for algebra to be 

# 66 for AAS.AOT
# 44 for CT.COM
# 44 for CT.PPL

# Write a Python program to access the Entrance Test Scores spreadsheet, update the test score, and then create a new spreadsheet called updatedScores.

# Create a dictionary for the test score updates and update the scores via a loop, increasing the row number to include all the rows in the spreadsheet.

# You can either hard code the dictionary into your program or import from a separate Python module. Do not change the formatting of the original spreadsheet. 

# Include some sort of user input validation. 

# *************************************************************************
import openpyxl, os, sys, time

def clearScreen():
    os.system("clear")
    
clearScreen()
# make desktop where files are saved / edited at
os.chdir("/Users/shawnconboy/Desktop")

# open the excel doc
wb = openpyxl.load_workbook("Entrance Test Scores.xlsx")
sheet = wb.active

# dictionary to replace scores
scoreUpdates = {
    "AAS.AOT": 66,
    "CT.COM": 44,
    "CT.PPL": 44
}

# loop through the rows 
for row in range(3, sheet.max_row + 1):  # Assuming data is from row 3 to 28
    acronym = sheet[f"B{row}"].value  # Column B has the Datatel Acronym

    if acronym in scoreUpdates:
        sheet[f"F{row}"].value = scoreUpdates[acronym]
        print(f"Updated {acronym} to {scoreUpdates[acronym]}")
    # else:
    #     print("Acronym not found.")

    # i thought this was the right move, but it flooded the console

# save a copy of updated data
print()
wb.save("updatedScores.xlsx")
print("File saved as updatedScores.xlsx")

time.sleep(2)
sys.exit()