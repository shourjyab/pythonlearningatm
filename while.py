spam=0
if spam<5:
    print ('hello world')
spam=spam+1

#re-enter the value to check while
print('enter a value')
value=input()
value=int(value)

while value<5:
    print('hello world will be printed '+str(value-1)+'times')
    value=value+1
