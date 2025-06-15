if len(urlList) > 0:
    print("Copied:")
    print("-"*20)
    print('\n'.join(urlList))
    pyperclip.copy('\n'.join(urlList))
else:
    print("No web addresses found."