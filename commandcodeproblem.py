#creates a list
spam=[]

#inputs observations into the list
while True:
    print('enter the item or press enter to stop input')
    item=input()
    if item=='': #to break out of the loop
        break
    spam=spam+[item] #converts the item into a list and adds it to the spam list
print(spam)

#end section is to ensure that all output is in one line
l=len(spam)
print('the lengh of the lost is:', end='')
print(l)

for i in range(l-2):
    print(spam[i]+',', end='')
print(spam[-2]+' and '+spam[-1])


    








 
