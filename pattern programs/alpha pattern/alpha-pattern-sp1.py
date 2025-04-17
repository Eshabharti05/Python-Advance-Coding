n=int(input('n value:-'))
space=n-1
number=1
for row in range(1,n+1):
    dummy=row
    for sp in range(1,space+1):
        print(' ',end=' ')
    for num in range(1,number+1):
        print(chr(64+dummy),end='   ')
    print()
    space-=1
    number+=1
'''output:-
n value:-9
                A
              B   B
            C   C   C
          D   D   D   D
        E   E   E   E   E
      F   F   F   F   F   F
    G   G   G   G   G   G   G
  H   H   H   H   H   H   H   H
I   I   I   I   I   I   I   I   I
'''