import os, shelve

os.system("clear")

os.chdir("/Users/shawnconboy/Desktop")

s = shelve.open("myData")

new = list(s.items())

print(new)