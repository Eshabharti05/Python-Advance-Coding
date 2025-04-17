n=int(input('n value:'))
space=0
star=1
dummy=1
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(dummy,end=' ')
        if row<=n//2:
            dummy+=2
            space+=1
        elif row==n//2+1:
            dummy-=1
            space-=1
        else:
            dummy-=2
            space-=1
    print()
'''output:-
n value:7
1
  3
    5
      7
    6
  4
2
'''