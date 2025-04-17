n=int(input('n value:-'))
space=n-1
number=1
odd=1
for row in range(1,n+1):
    dummy=odd
    for space in range(1,space+1):
        print(' ',end=' ')
    for num in range(1,number+1):
        print(dummy,end=' ')
        dummy+=1
    number+=1
    space-=1
    print()
    odd+=2
'''
n value:-5
        1
      3 4
    5 6 7
  7 8 9 10
9 10 11 12 13'''