n=int(input('n value:-'))
space=n-1
number=1
for row in range(1,n+1):
    dummy=row
    for sp in range(1,space+1):
        print(' ',end=' ')
    for num in range(1,number+1):
        print(dummy,end=' ')
    dummy-=1
    number+=1
    space-=1
    print()
'''output:-
n value:-5
        1
      2 2
    3 3 3
  4 4 4 4
5 5 5 5 5
'''
n=int(input('n value:-'))
space=n-1
number=1
dummy=n
for row in range(1,n+1):
    for space in range(1,space+1):
        print(' ',end=' ')
    for num in range(1,number+1):
        print(dummy,end=' ')
    dummy-=1
    number+=1
    space-=1
    print()
'''output:-
n value:-5
        5
      4 4
    3 3 3
  2 2 2 2
1 1 1 1 1
'''