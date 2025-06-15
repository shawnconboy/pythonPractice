import sys, os, pyperclip, time

os.system("clear")

message = {"agree": """Yeah. That sounds good.""",
           "busy": """Can't. I"m busy""",
           "later": """Definitely, later."""}

if len(sys.argv) < 2:
    print("Usage: py multiClip.py [keyphrase] - copy phrase text.")
    sys.exit()

keyphrase = "agree"

if keyphrase in message:
    pyperclip.copy(message[keyphrase])
    print("Text for " + keyphrase + " copied to the keyboard.")
else:
    print("There is no text for " + keyphrase)