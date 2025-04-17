n=int(input('n value:-'))
column=1
for row in range(1,n+1):
    dummy=1
    for col in range(1,column+1):
        print(chr(64+dummy),end=' ')
        dummy+=1
    print()
    column+=1
'''
output:-
n value:-5
A
A B
A B C
A B C D
A B C D E
'''
n=int(input('n value:-'))
column=1
for row in range(1,n+1):
    dummy=n
    for col in range(1,column+1):
        print(chr(64+dummy),end=' ')
        dummy-=1
    print()
    column+=1
'''
output:-
n value:-5
E
E D
E D C
E D C B
E D C B A
'''
n=int(input('n value:-'))
column=1
for row in range(1,n+1):
    dummy=row
    for col in range(1,column+1):
        print(chr(64+dummy),end=' ')
        dummy+=1
    print()
    column+=1
'''output:-
n value:-5
A
B C
C D E
D E F G
E F G H I
'''