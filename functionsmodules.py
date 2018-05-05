#importing the module called random

import random

#defining the function get answer
def getanswer(ansnum):
    if ansnum==1:
        return 'yes'
    elif ansnum==2:
        return 'no'
    elif ansnum==3:
        return 'maybe'

#assigning value of the random module to a variable
#random.randint(5,7) - will give random intgers between 5,6,7
r = random.randint(1,3)
proposal=getanswer(r)
print (proposal)

