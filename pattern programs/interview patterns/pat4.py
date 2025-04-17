#fibinacii series
n=int(input('n value:-'))
n1=2
n2=3
l=[]
for i in range(1,n+1):
    l.append(n1)
    res=n1+n2
    n1,n2=n2,res
space=0
star=1
ip=0
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(l[ip],end=' ')
    print()
    ip+=1
    if row<=n//2:
        space+=1
    else:
        space-=1 
'''output:-
n value:-9
2
  3
    5
      8
        13
      21
    34
  55
89
'''