# experimental programs trying to run the vampire program
#asks for name
print ('what is your name?')
#enter name
name=input()

print ('what is your age?')
#enter age
age=input()
age=int(age)

if name=='alice':
    print('hi alice you are '+str(age)+' years old')
elif age<=18:
    print('you are too young to be alice')
elif age>18 and age<=70:
    print('maybe you are alice and then again maybe not')
elif age>70:
    print('you are grandma!')

    

