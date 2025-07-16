# this is a hardcoded program that returns "H1" elements from a webpage.
# by swapping the website on line 15 and the specified elements on line 28
# this can become a reusable program.

import time, os, sys, bs4, requests

# function to clear screen for both mac or windows.
def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# clear screen, and print title of program
clearScreen()
print("Webscraper Program")
print("-"*42)
print()

# this line specifies what website you will be pulling from
getWebPage = requests.get("https://www.sccsc.edu/admissions-aid/apply/")

# this is a try and accept that tells you a reason for error if one were to occur
try:
    getWebPage.raise_for_status()
except Exception as ex:
    print(f"Error with page: {ex}")
    print("\nPlease enter correct webpage path")

    # end the program if error occured.
    time.sleep(3)
    sys.exit()

# here is the section divider to show findings
print("Found Items")
print("-"*42)
print()

# this line takes the HTML and converts it to one big text string
getWebPageSoup = bs4.BeautifulSoup(getWebPage.text, "html.parser")

# here is where you isolate your specified element
extractElements = getWebPageSoup.select("h1")
counter = 0

# and this is where we print the elements found to the console

for element in extractElements:
    print(f"{str(counter+1)}\t{element.text}")
    counter += 1
    print()
print(f"Elements found : {counter}")
print()

# ends the program
time.sleep(3)
sys.exit()
