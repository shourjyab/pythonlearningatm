#when coding from idle len needs a print statement
#creates a list named catNames
catnames=[]
while True:
    print('enter cat name '+ str(len(catnames)+1) + '(enter nothing to stop):')
    name=input()
    if name=='':
        break
    catnames=catnames+[name]
    print ('the names of the cats are')
    for name in catnames:
        print(name)


