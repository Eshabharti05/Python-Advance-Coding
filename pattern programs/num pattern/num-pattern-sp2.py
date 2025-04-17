n=int(input('n value:-'))
space=n-1
star=1
for row in range(1,n+1):
    dummy=row
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(dummy,end=' ')
        if st<=star//2:
            dummy-=1
        else:
            dummy+=1
    print()
    space-=1
    star+=2
'''output:-
n value:-5
        1
      2 1 2
    3 2 1 2 3
  4 3 2 1 2 3 4
5 4 3 2 1 2 3 4 5
'''
n=int(input('n value:-'))
space=n-1
star=1
for row in range(1,n+1):
    dummy=1
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(dummy,end=' ')
        if st<=star//2:
            dummy+=1
        else:
            dummy-=1
    print()
    space-=1
    star+=2
'''
output:-
n value:-5
        1
      1 2 1
    1 2 3 2 1
  1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
'''
n=int(input('n value:-'))
space=n-1
star=1
for row in range(1,n+1):
    dummy=row
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(dummy,end=' ')
        if st<=star//2:
            dummy+=1
        else:
            dummy-=1
    print()
    space-=1
    star+=2
'''outtput:-
n value:-5
        1
      2 3 2
    3 4 5 4 3
  4 5 6 7 6 5 4
5 6 7 8 9 8 7 6 5
'''
n=int(input('n value:-'))
space=n-1
star=1
for row in range(1,n+1):
    dummy=row
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(dummy,end=' ')
    print()
    if row<=n//2:
      space-=1
      star+=2
    else:
       space+=1
       star-=2
'''output:-
n value:-5
        1
      2 2 2
    3 3 3 3 3
      4 4 4
        5
'''
n=int(input('n value:-'))
space=n-1
star=1
for row in range(1,n+1):
    dummy=row
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    if row<=n//2:
      space-=1
      star+=2
    else:
       space+=1
       star-=2    
'''output:-
n value:-5
        1
      2 3 4
    3 4 5 6 7
      4 5 6
        5
'''
n=int(input('n value:-'))
space=n-1
star=1
dummy=1
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(dummy,end='  ')
        dummy+=1
    print()
    if row<=n//2:
      space-=1
      star+=2
    else:
       space+=1
       star-=2   
'''output:-
n value:-5
        1
      2  3  4
    5  6  7  8  9
      10  11  12
        13
'''