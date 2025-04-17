'''1   2   3   4   5
   16  17  18  19  6
   15  24  25  20  7
   14  23  22  21  8
   13  12  11  10  9'''
# (1,1)(1,2)(1,3)(1,4)(1,5)
# (2,1)(2,2)(2,3)(2,4)(2,5)
# (3,1)(3,2)(3,3)(3,4)(3,5)
# (4,1)(4,2)(4,3)(4,4)(4,5)
# (5,1)(5,2)(5,3)(5,4)(5,5)'''
n=int(input('n value:-'))
dummy=1
dummy1=16
for row in range(1,n+1):
   for  col in range(1,n+1):
      if row==1 or col==5:
         print(dummy,end='   ')
         dummy+=1
      elif col==1 or row==5:
         print(dummy1,end='  ')
         dummy1-=1
      else:
         print(' ',end='   ')
   print()
      

            