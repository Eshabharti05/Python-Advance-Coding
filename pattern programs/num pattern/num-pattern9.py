n=int(input('n value:-'))
space=0
number=n
for row in range(1,n+1):
    dummy=row
    for sp in range(1,space+1):
        print(' ',end=' ')
    for num in range(1,number+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    space+=1
    number-=1
'''output:-
n value:-5
1 2 3 4 5
  2 3 4 5
    3 4 5
      4 5
        5
'''
n=int(input('n value:-'))
space=0
number=n
for row in range(1,n+1):
    dummy=row
    for sp in range(1,space+1):
        print(' ',end=' ')
    for num in range(1,number+1):
        print(dummy,end=' ')
    dummy+=1
    print()
    space+=1
    number-=1
'''output:-
n value:-5
1 1 1 1 1
  2 2 2 2
    3 3 3
      4 4
        5
'''