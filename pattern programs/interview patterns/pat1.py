n=int(input('n value:'))
space=0
star=1
dummy=1
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    if row<=n//2:
        space+=1
    else:
        space-=1
'''output:-
n value:5
1
  2
    3
  4
5
'''