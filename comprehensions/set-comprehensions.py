#SETCOMPREHENSION:-
#set comprehension is used to create a new set from an existing iterable/SEQUENCE
'''1st scenario:-
            set comprehension using 1 value and 1 for loop
            syntax:-varname=[value for loop]'''
# ex:-adding numbers in set using set comprehensions
# s={i for i in range(1,6)}
# print(s) #output:-{1, 2, 3, 4, 5}
'''2nd scenario:-
            set comprehension with 1vale and 1for loop and 1if conditon
            syntax:-varname=[value for loop if condition]'''
#ex:-add odd numbers from a list
l=[11,22,33,44,55,66]
s={i for i in l if i%2!=0}
print(s) #output:-{33, 11, 55}
'''3rd scenario:-
            set comprehension with 1value and 1for loop and mulitple if conditions
            syntax:-varname=[value for loop if condition1 and/or if condition2]'''
#ex:-add even numbers and odd numbers if greater than 30 from the list
l=[11,22,33,44,55,66]
s={i for i in l if i%2==0 or i>30}
print(s) #output:-{33, 66, 44, 22, 55}
'''4th scenario:-
            set comprehension with 1value and 1for loop and if else condition(ternery operation)
            syntax:-varname=[value truevalue if condition else falsevalue for loop]'''
#ex:-add 1 to set if even numbers and 0 to the set if odd numbers from the list
l1=[11,22,33,44,55,66]
s={ 1 if i%2==0 else 0 for i in l1 }
print(s) #output:-{0,1} here there are duplicates so prefer list comprehwnsion here
'''5th scenario:-
            set comprehension with 1value and nested/multiplefor loop and if conditions
            syntax:-varname=[value for loop1 for loop2-----for loopn if condition]'''
#ex:-add even numbers and odd numbers if greater than 30 from the list
outputexpected={(1,1,1),(2,2,2),(3,3,3),(4,4,4),(5,5,5)}
s={(i,j,k) for i in range(1,6) for j in range(1,6) for k in range(1,6) if i==j==k}
print(s) #output:-{(5, 5, 5), (2, 2, 2), (3, 3, 3), (4, 4, 4), (1, 1, 1)}