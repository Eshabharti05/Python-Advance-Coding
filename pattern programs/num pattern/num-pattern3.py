n=int(input('n value:-'))
dummy=1
column=1
for row in range(1,n+1):
    for col in range(1,column+1):
        print(dummy,end=' ')
    dummy+=1
    print()
    column+=1
'''
output:-
n value:-5
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
n=int(input('n value:-'))
dummy=n
column=1
for row in range(1,n+1):
    for col in range(1,column+1):
        print(dummy,end=' ')
    dummy-=1
    print()
    column+=1
'''output:-
n value:-5
5
4 4
3 3 3
2 2 2 2
1 1 1 1 1
'''