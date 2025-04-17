n=int(input('n value:-'))
column=n
dummy=1
for row in range(1,n+1):
    for col in range(1,column+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    column-=1
'''output:-
n value:-5
1 2 3 4 5
6 7 8 9
10 11 12
13 14
15
'''
n=int(input('n value:-'))
column=n
dummy=1
for row in range(1,n+1):
    for col in range(1,column+1):
        print(dummy,end=' ')
    dummy+=1
    print()
    column-=1
'''output:-
n value:-5
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5
'''