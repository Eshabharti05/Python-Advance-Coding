n=int(input('n value:-'))
space=n-1
number=1
for row in range(1,n+1):
    dummy=row
    for space in range(1,space+1):
        print(' ',end=' ')
    for num in range(1,number+1):
        print(chr(64+dummy),end=' ')
        dummy-=1
    number+=1
    space-=1
    print()
'''output:-
n value:-5
        A
      B A
    C B A
  D C B A
E D C B A
'''
n=int(input('n value:-'))
space=n-1
number=1
for row in range(1,n+1):
    dummy=n
    for space in range(1,space+1):
        print(' ',end=' ')
    for num in range(1,number+1):
        print(chr(64+dummy),end=' ')
        dummy-=1
    number+=1
    space-=1
    print()
'''output:-
n value:-5
        E
      E D
    E D C
  E D C B
E D C B A
'''    