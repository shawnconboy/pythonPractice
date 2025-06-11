import time, os, sys

os.system("clear")

catNames = []

while True:
    name = input (f'Enter name of cat {len (catNames)+1} or end to stop ')
    if name == 'end':
        break
    catNames.append (name)

for i in catNames:
    print(i)

newCat = input ('Enter name of cat ')
if newCat not in catNames: 
    catNames.append (newCat)
print ('The cat names are ')

for n in catNames:
    print(n)


