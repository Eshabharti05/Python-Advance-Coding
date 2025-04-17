
'''output:-
* 
* *
* * *
* * *
* *
*
'''   
n=6
star=0
space=0
for row in range(1,n//2+1):
    star+=1
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print('*',end=' ')
    print()
for row in range(n//2+1,n+1):
    star-=1
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print('*',end=' ')
    print()
        