#generic method:-
n=int(input('enter n:-'))
star=1
space=n-1
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print('*',end=' ')
    print()
    star+=2
    space-=1
'''output:-
enter n:-3
    *
  * * *
* * * * *
enter n:-5
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
enter n:-9
                *
              * * *
            * * * * *
          * * * * * * *
        * * * * * * * * *
      * * * * * * * * * * *
    * * * * * * * * * * * * *
  * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * *
''' 