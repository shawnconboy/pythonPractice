# this is a website extractionator

# terribly pieced together by Shawn Conboy
# ...


# import the stuff we need.
import re, pyperclip, time, os, sys

def clear():
    time.sleep(2)
    os.system("cls" if os.name == "nt" else "clear")

clear()
# handy dandy www.website.com fancy structure thingy mabob.
urlRegex = re.compile(r"""
    https?://               # http or https
    www\.                   # www.
    [a-zA-Z0-9_%+-]+        # google
    \.                      # .
    [a-zA-Z]{2,4}           # .com .co .whatsitooya
""", re.VERBOSE)

# this is a subtle hint to the user -- "copy a doc to search it"
print("Psst.")
clear()
print("Hey...")
clear()
print("Copy a document to begin search.")
time.sleep(2)
input("Hit enter when you have the file copied to your clipboard.")


# Get text from the clipboard
data = pyperclip.paste()

# Find all URL matches using findall()
foundUrls = urlRegex.findall(data)

# Store matches in a list
urlList = []
for i in foundUrls:
    urlList.append(i)

print()
# Print results and copy them to clipboard
# if found matches is greater than 0, something
# matching our criteria has been found
if len(urlList) > 0:
    print("Copied:")
    print("-"*20)
    print('\n'.join(urlList))
    pyperclip.copy('\n'.join(urlList))
else:
    print("No web addresses found.")

print("\n\nProgram ended.")

time.sleep(5)
sys.exit()