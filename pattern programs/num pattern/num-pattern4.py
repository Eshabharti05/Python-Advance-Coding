n=int(input('n value:-'))
column=1
for row in range(1,n+1):
    dummy=1
    for col in range(1,column+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    column+=1
'''
output:-
n value:-5
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
n=int(input('n value:-'))
column=1
for row in range(1,n+1):
    dummy=n
    for col in range(1,column+1):
        print(dummy,end=' ')
        dummy-=1
    print()
    column+=1
'''
output:-
n value:-5
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
'''
n=int(input('n value:-'))
column=1
for row in range(1,n+1):
    dummy=row
    for col in range(1,column+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    column+=1
'''output:-
n value:-5
1
2 3
3 4 5
4 5 6 7
5 6 7 8 9
'''