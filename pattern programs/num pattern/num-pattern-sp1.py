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
'''output:-
n value:-3
    1
  2  2
3  3  3
n value:-5
        1
      2   2
    3   3   3
  4   4   4   4
5   5   5   5   5
n value:-9
                1
              2   2
            3   3   3
          4   4   4   4
        5   5   5   5   5
      6   6   6   6   6   6
    7   7   7   7   7   7   7
  8   8   8   8   8   8   8   8
9   9   9   9   9   9   9   9   9
'''