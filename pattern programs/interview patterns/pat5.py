#prime number
n=int(input('n value:'))
c=0
n1=2
l=[]
while c<n:
    for i in range(2,n1//2+1):
        if n1%i==0:
            break
    else:
        l.append(n1)
        c+=1  
    n1+=1
print(l)       
space=0
star=1
ip=0
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print(l[ip],end=' ')
    ip+=1
    print()
    if row<=n//2:
        space+=1
    else:
        space-=1 
'''output:-
n value:9
[2, 3, 5, 7, 11, 13, 17, 19, 23]
2
  3
    5
      7
        11
      13
    17
  19
23
'''
            
    
