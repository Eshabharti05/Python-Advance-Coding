'''expected output:-
n value:-5
A
  B
    C
      D
        E
'''
n=int(input('n value:-'))
dummy=1
for row in range(1,n+1):
    for col in range(1,n+1):
        if row==col:
            print(chr(64+dummy),end=' ')
            dummy+=1
        else:
            print(' ',end=' ')
    print()
#generic method:-
n=int(input('n value:-'))
space=0
num=1
dummy=1
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for num in range(1,num+1):
        print(chr(64+dummy),end=' ')
    print()
    dummy+=1
    space+=1
'''output:-
n value:-5
A
  B
    C
      D
        E
'''
#generic method:-
n=int(input('n value:-'))
space=0
num=1
dummy=5
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for num in range(1,num+1):
        print(chr(64+dummy),end=' ')
    print()
    dummy-=1
    space+=1
'''output:-
n value:-5
E
  D
    C
      B
        A
'''
