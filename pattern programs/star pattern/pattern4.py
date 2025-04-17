# normal method ---1
#row to col
n=5
for row in range(1,n+1):
    for col in range(1,n+1):
        if row<=col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#generic method
n=5
space=0
star=n
for row in range(1,n+1):
    for space in range(1,space+1):
        print(' ',end=' ')
    for star in range(1,star+1):
        print('*',end=' ')
    star-=1
    space+=1
    print()
'''output:-
* * * * *
  * * * *
    * * *
      * *
        *
'''
    
