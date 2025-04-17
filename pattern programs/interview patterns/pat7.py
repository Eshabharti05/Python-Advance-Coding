n=2
l=[]
c=0
while c<15:
    for i in range(2,n//2+1):
        if n%i==0:
            break
    else:
        c+=1
        l.append(n)
    n+=1
n1=int(input('enter n value:-'))
star=1
ip=0
for row in range(1,n1+1):
    for star in range(1,star+1):
        print(l[ip],end=' ')
        ip+=1
    print()
    star+=1
'''output:- n=5
2
3 5
7 11 13
17 19 23 29
31 37 41 43 47
'''