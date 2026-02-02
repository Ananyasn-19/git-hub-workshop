# tup1=(1,2,3,4)
# print(tup1)
# tup2=() creating empty tuple
#u can create tuple with mixed data types
# tup1=(1,"hello",3.4,True)

# a,b=10,20
# print(a,b)any comma separated values without parentheses or [] is considered as tuple by default

#to create tuple with single element "comma" is must
# tup3=(10,) #single element tuple

# divmod(10,3) #returns tuple containing quotient and remainder it is a built in function
# print(divmod(10,3)) #(3,1)

# accesing elements of tuple
# tup1=(1,2,3,4,5)    
# print(tup1[0]) #1
# print(tup1[-1]) #5
# print(tup1[1:4]) #(2,3,4)   
# print(tup1[:3]) #(1,2,3)
# print(tup1[:]) #(1,2,3,4,5)

# updating tuple
# tup1=(1,2,3,4)
# tup2=(5,6)
# tup3=tup1+tup2
# print(tup3)
   
# deleting tuple
# tup1=(1,2,3,4)
# # del tup1[3]
# # print(tup1) #tuples are immutable so we cant delete or update elements of tuple
# del tup1
# print(tup1)

# basic tuple operations
# len((1,2,3))
# (1,2,3)+(4,5) #(1,2,3,4,5)
# ("good")*3 #"goodgoodgood"
# 5 in (1,2,3,4,5) #true memebership operator
# for i in (1,2,3,4):

#     print(i,end=' ') #1 2 3 4
# comparision, true and false
# (1,2,3)<(1,2,4) #true
# max((1,2,3)) #3
# min((1,2,3)) #1

# print(tuple("hello")) convertint an sequence into tuple 
# print(tuple([1,2,3,4])) converting list into tuple (1,2,3,4)
# print(tuple({1,2,3,4})) #converting set into tuple (1,2,3,4)
# print(tuple({"name":"john","age":25})) #converting dictionary into tuple ('name','age') only keys are considered

# tuple assignments
# expression are evaluated first and then assigned to the variables on left side
# tup1=(100,200,300)
# val1,val2,val3=tup1
# print(val1)
# (val1,val2,val3)=(10%2,10+7,2-2)
# print(val1)
# numberof values must be same on both sides during tuple assignment otherwise it will throw value error


# tuples for returning multiple values from a function
# def max_min(vals):
#     x=max(vals)
#     y=min(vals)
#     return(x,y)
# vals=(10,3,5,7,2)
# (max_marks,min_marks)=max_min(vals)

# print("max:",max_marks)
    