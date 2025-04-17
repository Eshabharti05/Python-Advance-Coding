n=int(input('n value:-'))
dummy=1
column=1
for row in range(1,n+1):
    for col in range(1,column+1):
        print(chr(64+dummy),end=' ')
    dummy+=1
    print()
    column+=1
'''
output:-
n value:-5
A
B B
C C C
D D D D
E E E E E
'''
n=int(input('n value:-'))
dummy=n
column=1
for row in range(1,n+1):
    for col in range(1,column+1):
        print(chr(64+dummy),end=' ')
    dummy-=1
    print()
    column+=1
'''output:-
n value:-5
E
D D
C C C
B B B B
A A A A A
'''