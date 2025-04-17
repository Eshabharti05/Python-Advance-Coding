n=int(input('n value:-'))
space=n-1
star=1
for row in range(1,n+1):
    dummy=row
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(chr(64+dummy),end=' ')
        if st<=star//2:
            dummy-=1
        else:
            dummy+=1
    print()
    space-=1
    star+=2
'''output:-
n value:-5
        A
      B A B
    C B A B C
  D C B A B C D
E D C B A B C D E
'''
n=int(input('n value:-'))
space=n-1
star=1
for row in range(1,n+1):
    dummy=1
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(chr(64+dummy),end=' ')
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
        A
      A B A
    A B C B A
  A B C D C B A
A B C D E D C B A
'''
n=int(input('n value:-'))
space=n-1
star=1
for row in range(1,n+1):
    dummy=row
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(chr(64+dummy),end=' ')
        if st<=star//2:
            dummy+=1
        else:
            dummy-=1
    print()
    space-=1
    star+=2
'''outtput:-
n value:-5
        A
      B C B
    C D E D C
  D E F G F E D
E F G H I H G F E     
'''
n=int(input('n value:-'))
space=n-1
star=1
for row in range(1,n+1):
    dummy=row
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(chr(64+dummy),end=' ')
    print()
    if row<=n//2:
      space-=1
      star+=2
    else:
       space+=1
       star-=2
'''output:-
n value:-5
        A
      B B B
    C C C C C
      D D D
        E    
'''
n=int(input('n value:-'))
space=n-1
star=1
for row in range(1,n+1):
    dummy=row
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(chr(64+dummy),end=' ')
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
        A
      B C D
    C D E F G
      D E F
        E
'''
n=int(input('n value:-'))
space=n-1
star=1
dummy=1
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(chr(64+dummy),end=' ')
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
        A
      B C D
    E F G H I
      J K L
        M
'''