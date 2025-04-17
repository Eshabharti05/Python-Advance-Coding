# print alphabets in apattern is same as number pattern
#but here we need to use chr(64+dummy,end=' ') instead of dummy
#EX:-
n=int(input('n value:-'))
space=n-1
number=1
for row in range(1,n+1):
    dummy=row
    for sp in range(1,space+1):
        print(' ',end=' ')
    for num in range(1,number+1):
        print(dummy,end='   ')
    print()
    space-=1
    number+=1
'''OUTPUT:-
n value:-5
        1
      2   2
    3   3   3
  4   4   4   4
5   5   5   5   5
'''
#but after using chr(64+)
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
n value:-5
        A
      B   B
    C   C   C
  D   D   D   D
E   E   E   E   E
n value:-11
                    A
                  B   B
                C   C   C
              D   D   D   D
            E   E   E   E   E
          F   F   F   F   F   F
        G   G   G   G   G   G   G
      H   H   H   H   H   H   H   H
    I   I   I   I   I   I   I   I   I
  J   J   J   J   J   J   J   J   J   J
K   K   K   K   K   K   K   K   K   K   K
'''