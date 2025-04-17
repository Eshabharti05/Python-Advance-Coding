# '''1st type in number patterns'''
# n=int(input('n value:-'))
# dummy=1
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         print(dummy,end=' ')
#         dummy+=1
#     print()
# '''output:-
# n value:-5
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25
# '''
# '''2nd type in number patterns'''
# n=int(input('n value:-'))
# for row in range(1,n+1):
#     dummy=1
#     for col in range(1,n+1):
#         print(dummy,end=' ')
#         dummy+=1
#     print()
# '''output:-
# n value:-5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# '''
# '''3rd type in number patterns'''
# n=int(input('n value:-'))
# dummy=1
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         print(dummy,end=' ')
#     print()
#     dummy+=1
# '''output:-
# n value:-5
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5
# '''
# '''4th type in number patterns'''
# n=int(input('n value:-'))
# for row in range(1,n+1):
#     dummy=row
#     for col in range(1,n+1):
#         print(dummy,end=' ')
#         dummy+=1
#     print()
# '''output:-
# n value:-5
# 1 2 3 4 5
# 2 3 4 5 6
# 3 4 5 6 7
# 4 5 6 7 8
# 5 6 7 8 9
# '''
'''another type in number patterns'''
n=int(input('n value:-'))
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(dummy,end=' ')
        dummy+=5
    print()
'''output:-
n value:-5
1 6 11 16 21
2 7 12 17 22
3 8 13 18 23
4 9 14 19 24
5 10 15 20 25
'''


 



