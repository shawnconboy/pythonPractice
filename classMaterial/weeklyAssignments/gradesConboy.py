# This program will create a grade report for any number of students
import time, os, sys

# multiple os compatible funciton to clear screen
def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# simple header
def displayInfo():
    print("Central Community College")
    print("CPT 277 Advanced Python Programming")
    print("-"*50)

def nextSection():
    clearScreen()
    displayInfo()

# main loop(per student)
response = "y"
while response == "y":
    nextSection()
    name = input("\nPlease enter your name : ")

    # quiz section. gets user data.
    quizGradeContinue = "y"
    quizGradeTotal = 0
    quizCounter = 0

    while quizGradeContinue == 'y':
        quizGrade = float(input("Please enter quiz grade : "))

        if quizGrade > 110:
            print("Grade must not exceed 110. Try again.")
            time.sleep(2)
            continue
        elif quizGrade < 0:
            print("Grade must be no less than 0.")
            time.sleep(2)
            continue

        quizGradeTotal = quizGrade + quizGradeTotal
        quizCounter = quizCounter + 1
        quizGradeContinue = input("Do you have another quiz grade to enter? (Y/N) : ")

    quizAverage = quizGradeTotal / quizCounter

    # final project section
    nextSection()
    finalProjectGrade = float(input("\nPlease enter your final project grade : "))

    # if finalProjectGrade > 110:
    #     print("Grade must not exceed 110. Try again.")
    #     time.sleep(2)
    #     continue
    # elif finalProjectGrade < 0:
    #     print("Grade must be no less than 0.")
    #     time.sleep(2)
    #     continue

    # currently unsure of how to get this working correctly.

    # final exam section
    nextSection()
    finalExamGrade = float(input("\nPlease enter your final exam grade : "))

    # this takes and applies correct percentages for overall grade
    overallGrade = (quizAverage * 0.5) + (finalProjectGrade * 0.3) + (finalExamGrade * 0.2)

    # data is printed to console here
    nextSection()
    print(f"{'Student Name':<30}{name:>18}")
    print(f"\n{'Quiz Average':<30}{quizAverage:>18.2f}")
    print(f"{'Final Project Grade':<30}{finalProjectGrade:>18.2f}")
    print(f"{'Final Exam Grade':<30}{finalExamGrade:>18.2f}")
    print(f"{'Overall Grade':<30}{overallGrade:>18.2f}")

    # push all student data to a .txt file
    cleanName = name.replace(" ","_")
    filePath = (f"/Users/shawnconboy/Desktop/{cleanName}_GradeReport.txt")

    # Open the file manually
    file = open(filePath, "w")

    # Write to the file
    file.write("\t    Central Community College\n")
    file.write("\tCPT 277 Advanced Python Programming\n")
    file.write("-" * 50 + "\n")
    file.write(f"{'Student Name':<30}{name:>18}\n\n")
    file.write(f"{'Quiz Average':<30}{quizAverage:>18.2f}\n")
    file.write(f"{'Final Project Grade':<30}{finalProjectGrade:>18.2f}\n")
    file.write(f"{'Final Exam Grade':<30}{finalExamGrade:>18.2f}\n")
    file.write(f"\n{'Overall Grade':<30}{overallGrade:>18.2f}\n")

    # Always remember to close the file manually
    file.close()

    print("Report created.")

    response = input("\nCreate report for a new student? (Y/N) : ").lower()

print("Thank you. Program has ended.")
time.sleep(3)
sys.exit()