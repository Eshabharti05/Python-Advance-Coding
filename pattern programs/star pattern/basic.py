# '''EX:- for n=5
# (1,1)(1,2)(1,3)(1,4)(1,5)
# (2,1)(2,2)(2,3)(2,4)(2,5)
# (3,1)(3,2)(3,3)(3,4)(3,5)
# (4,1)(4,2)(4,3)(4,4)(4,5)
# (5,1)(5,2)(5,3)(5,4)(5,5)'''
# # (Q)  1ST METHOD:-
# n=5
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         print('*',end=' ')
#     print()
# #    2nd method:-
# n=5
# for row in range(1,n+1):
#     print('* '*n)
'''1st type in number patterns'''
n=int(input('n value:-'))
dummy=1
for row in range(1,n+1):
    for col in range(1,n+1):
        print(dummy,end=' ')
        dummy+=1
    print()
'''output:-
n value:-5
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
'''
'''2nd type in number patterns'''
n=int(input('n value:-'))
# dummy=1
for row in range(1,n+1):
    dummy=1
    for col in range(1,n+1):
        print(dummy,end=' ')
        dummy+=1
    print()

 



