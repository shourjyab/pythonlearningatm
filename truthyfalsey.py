#to see the function of truthy falset statements
name='joe'
print ('who are you')
name=input()

while name!='joe':
    print ('user not found')
    print ('enter name again')
    name=input()
print ('hello joe what is the password')
password=input()
if password=='swordfish':
    print ('access granted')
else:
    print ('access denied')
