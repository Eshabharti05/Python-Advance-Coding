'''expected output:-
n value:-5
1
  2
    3
      4
        5
'''
n=int(input('n value:-'))
dummy=1
for row in range(1,n+1):
    for col in range(1,n+1):
        if row==col:
            print(dummy,end=' ')
            dummy+=1
        else:
            print(' ',end=' ')
    print()
#generic method:-
n=int(input('n value:-'))
space=0
num=1
dummy=1
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for num in range(1,num+1):
        print(dummy,end=' ')
    print()
    dummy+=1
    space+=1
'''output:-
n value:-5
1
  2
    3
      4
        5
'''
#generic method:-
n=int(input('n value:-'))
space=0
num=1
dummy=5
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for num in range(1,num+1):
        print(dummy,end=' ')
    print()
    dummy-=1
    space+=1
'''output:-
n value:-5
5
  4
    3
      2
        1
'''
