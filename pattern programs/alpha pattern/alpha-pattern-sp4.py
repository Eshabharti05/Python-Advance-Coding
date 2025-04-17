n=int(input('n value:-'))
space=n-1
number=1
odd=1
for row in range(1,n+1):
    dummy=odd
    for space in range(1,space+1):
        print(' ',end=' ')
    for num in range(1,number+1):
        print(chr(64+dummy),end=' ')
        dummy+=1
    number+=1
    space-=1
    print()
    odd+=2
'''
n value:-5
        A 
      C D
    E F G
  G H I J
I J K L M
'''