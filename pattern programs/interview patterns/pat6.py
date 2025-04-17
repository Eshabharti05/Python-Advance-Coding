s=input('enter a string:-')
dummy=list(set(sorted(s)))
# dummy=s
star=1
space=len(s)*2-1
for row in range(len(dummy)):
    i=0
    for space in range(1,space+1):
        print(' ',end=' ')
    for star in range(1,star+1):
        print(dummy[i],end=' ')
        i+=1
    print()
    space-=2
    star+=1
'''output:-
enter a string:-charan
                      a 
                  a n
              a n c
          a n c r
      a n c r h
'''