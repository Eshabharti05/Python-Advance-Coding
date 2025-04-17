# in solving thesee programs generic method is not used
n=int(input('n value:-'))
for i in range(1,n+1):
    dummy=i
    for j in range(1,n+1):
        if i==j or i+j==n+1:
            print(dummy,end=' ')
        else:
            print(' ',end=' ')
    print()
'''output:-
n value:-5
1       1
  2   2
    3
  4   4
5       5
'''
n=int(input('n value:-'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==n//2+1:
            print(j,end=' ')
        elif j==n//2+1:
            print(i,end=' ')
        else:
            print(' ',end=' ')
    print()
'''output:-
n value:-9
        1
        2
        3
        4
1 2 3 4 5 6 7 8 9
        6
        7
        8
        9
'''
n=int(input('n value:-'))
for i in range(1,n+1):
    dummy=n
    for j in range(1,n+1):
        print(dummy,end=' ')
        if i>j:
            dummy-=1
    print()
'''output:-
n value:-5
5 5 5 5 5
5 4 4 4 4
5 4 3 3 3
5 4 3 2 2
5 4 3 2 1
'''