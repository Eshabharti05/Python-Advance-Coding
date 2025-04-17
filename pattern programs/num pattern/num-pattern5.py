n=int(input('n value:-'))
space=n-1
number=1
for row in range(1,n+1):
    dummy=row
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
        1
      2 1
    3 2 1
  4 3 2 1
5 4 3 2 1
'''
n=int(input('n value:-'))
space=n-1
number=1
for row in range(1,n+1):
    dummy=n
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
      5 4
    5 4 3
  5 4 3 2
5 4 3 2 1
'''       
        
