import re, pyperclip, time, sys, os

def clearScreen():
    os.system("clear")

phoneRegex = re.compile(r"""
(\d{3})-(\d{3}-\d{4})                        
""",re.VERBOSE)

phoneMatch = pyperclip.paste()