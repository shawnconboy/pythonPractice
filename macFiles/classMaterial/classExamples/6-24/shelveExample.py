import os, shelve
os.chdir("/Users/shawnconboy/Desktop")

shelveVariable = shelve.open("myData")

cats = ["abby", "barry", "colleen"]

dogs = ["rocky", "steve", "tony"]

shelveVariable["cats"] = cats
shelveVariable["dogs"] = dogs

shelveVariable.close()