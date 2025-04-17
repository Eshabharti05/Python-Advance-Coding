# in solving thesee programs generic method is not used
n=int(input('n value:-'))
for i in range(1,n+1):
    dummy=i
    for j in range(1,n+1):
        if i==j or i+j==n+1:
            print(chr(64+dummy),end=' ')
        else:
            print(' ',end=' ')
    print()
'''output:-
n value:-5
A       A
  B   B
    C
  D   D
E       E
'''
n=int(input('n value:-'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==n//2+1:
            print(chr(64+j),end=' ')
        elif j==n//2+1:
            print(chr(64+i),end=' ')
        else:
            print(' ',end=' ')
    print()
'''output:-
n value:-9
        A
        B
        C
        D
A B C D E F G H I
        F
        G
        H
        I
'''
n=int(input('n value:-'))
for i in range(1,n+1):
    dummy=n
    for j in range(1,n+1):
        print(chr(64+dummy),end=' ')
        if i>j:
            dummy-=1
    print()
'''output:-
n value:-5
E E E E E
E D D D D
E D C C C
E D C B B
E D C B A
'''