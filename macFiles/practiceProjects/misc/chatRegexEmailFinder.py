import time, os, sys, re, pyperclip

os.system("clear")

# Define the email regex pattern
emailRegex = re.compile(r"\w+@\w+\.\w{2,4}")

# Get clipboard data
sampleData = pyperclip.paste()

# Find all email matches
foundMatches = emailRegex.findall(sampleData)

# Print the results
if len(foundMatches) > 0:
    print("✔ Found email(s):")
    for email in foundMatches:
        print("-", email)
    
    # Optional: Copy results back to clipboard
    pyperclip.copy('\n'.join(foundMatches))
    print("\nCopied to clipboard.")
else:
    print("❌ No matches found.")