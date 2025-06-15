import pyperclip, re, time, sys, os

# os.system("clear")

# phoneRegex = re.compile('\d\d\d-\d\d\d-\d\d\d\d')

# phoneMatch = phoneRegex.search("My number is 864-431-5531")

# # print(phoneMatch)
# # print(phoneMatch.group())

# phoneRegex = re.compile(r"((\d\d\d)-(\d\d\d-\d\d\d\d))")
# print(phoneMatch.group())
# # print(phoneMatch.group(1))
# # print(phoneMatch.group(2))

# # areaCode, mainNumber = phoneMatch.groups()

# # print(areaCode)
# # print(mainNumber)

os.system("clear")

baldwinFamily = re.compile(r"([A-Z])([a-z]+)\s(Baldwin)")

mo = baldwinFamily.search("Sue Baldwin is a good man")

print(mo.group())
print()


print(mo.group(1))

print()

print(mo.group(2))

time.sleep(4)
sys.exit()