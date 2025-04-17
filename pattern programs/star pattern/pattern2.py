# normal method ---1
#row+col to n+1
n=5
for row in range(1,n+1):
    for col in range(1,n+1):
        if row+col>=n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#generic method
n=5
space=n-1
star=1
for row in range(1,n+1):
    for space in range(1,space+1):
        print(' ',end=' ')
    for star in range(1,star+1):
        print('*',end=' ')
    space-=1
    star+=1
    print()
    
'''output:-
        *
      * *
    * * *
  * * * *
* * * * *
'''