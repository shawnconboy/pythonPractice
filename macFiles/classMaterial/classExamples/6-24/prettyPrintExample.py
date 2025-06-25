import pprint, os


os.system("clear")
os.chdir("/Users/shawnconboy/Desktop")

birthdays = {"Bob": "April 2", "Harry": "June 24", "Rich": "October 19"}

birthdayFile = open("birthdayFile.py", "w")

birthdayFile.write("birthdays = " + pprint.pformat(birthdays))

birthdayFile.close()