n=int(input('n value:-'))
column=n
for row in range(1,n+1):
    dummy=1
    for col in range(1,column+1):
        print(chr(64+dummy),end=' ')
        dummy+=1
    print()
    column-=1
'''output:-
n value:-5
A B C D E
A B C D
A B C
A B
A
'''
n=int(input('n value:-'))
column=n
for row in range(1,n+1):
    dummy=5
    for col in range(1,column+1):
        print(chr(64+dummy),end=' ')
        dummy-=1
    print()
    column-=1
'''output:-
n value:-5
E D C B A
E D C B
E D C
E D
E
'''