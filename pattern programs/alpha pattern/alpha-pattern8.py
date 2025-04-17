n=int(input('n value:-'))
column=n
dummy=1
for row in range(1,n+1):
    for col in range(1,column+1):
        print(chr(64+dummy),end=' ')
        dummy+=1
    print()
    column-=1
'''output:-
n value:-5
A B C D E
F G H I
J K L
M N
O
'''
n=int(input('n value:-'))
column=n
dummy=1
for row in range(1,n+1):
    for col in range(1,column+1):
        print(chr(64+dummy),end=' ')
    dummy+=1
    print()
    column-=1
'''output:-
n value:-5
A A A A A
B B B B
C C C
D D
E
'''