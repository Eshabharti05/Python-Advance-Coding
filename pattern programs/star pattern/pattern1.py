# normal method ---1
# row to col
n=5
for row in range(1,n+1):
    for col in range(1,n+1):
        if row>=col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
# normal method ---2
n=5
for row in range(1,n+1):
    print('* '*row)
# normal method ---3
n=5
for row in range(1,n+1):
    for col in range(1,row+1):
        print('*',end=' ')
    print()
# generic method 
n=5
star=1
space=0
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print('*',end=' ')
    star+=1
    print()

'''output:-
*
* *
* * *
* * * *
* * * * *
'''