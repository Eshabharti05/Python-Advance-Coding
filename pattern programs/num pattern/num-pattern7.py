n=int(input('n value:-'))
column=n
for row in range(1,n+1):
    dummy=1
    for col in range(1,column+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    column-=1
'''output:-
n value:-5
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''
n=int(input('n value:-'))
column=n
for row in range(1,n+1):
    dummy=5
    for col in range(1,column+1):
        print(dummy,end=' ')
        dummy-=1
    print()
    column-=1
'''output:-
n value:-5
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
'''