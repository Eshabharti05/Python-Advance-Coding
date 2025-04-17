#generic method:-
n=int(input('enter n:-'))
star=1
space=0
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print('*',end=' ')
    print()
    if row<=n//2:
        star+=2
    else:
        star-=2
'''output:-
if n=9
*
* * *
* * * * *
* * * * * * *
* * * * * * * * *
* * * * * * *
* * * * *
* * *
*
'''