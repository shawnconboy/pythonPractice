#Program to demonstrate returning a value from a function
import random
#Function to return a fortune based on number in Magic 8 Ball 
def get_answer (answer) :
    if answer ==1:
        return 'It is certain'
    elif answer ==2:
        return 'It is decidedly so'
    elif answer ==3:
        return 'Yes'
    elif answer ==4:
        return 'Reply is hazy try again'
    elif answer ==5:
        return 'Ask again later'
    else:
        return 'Concentrate and ask again'
    

#Main program
#Generate a random number and then retrieve fortune from function
r = random.randint (1, 6)
fortune = get_answer (r)
print (fortune)