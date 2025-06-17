import re, time, os, sys, pyperclip

def clearScreen():
    os.system("clear")

clearScreen()

# Define the regex pattern with re.VERBOSE for readability
phoneRegex = re.compile(r"""(
    (\d{3})     # area code
    -           # hyphen
    (\d{3})     # first 3 digits
    -           # hyphen
    (\d{4})     # last 4 digits
)""", re.VERBOSE)

# Grab full page text from clipboard
phoneSearch = pyperclip.paste()

# Find all matches
phoneMatches = phoneRegex.findall(phoneSearch)

# Extract only the full match from each tuple
results = [match[0] for match in phoneMatches]

# Output results
if results:
    print("Phone numbers found:")
    print("-" * 20)
    for number in results:
        print(number)
    pyperclip.copy('\n'.join(results))
    print("\nCopied to clipboard!")
else:
    print("No phone numbers found.")
