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
a=0.1
b=0.2
c=0.3
print(a+b==c)