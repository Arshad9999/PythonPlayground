#FactorialFunction
#import math as m
num=int(input("Enter the number : "))
#result=m.factorial(num)
def fact(n):
  if n<=1:
    return 1
  else:
    return n*fact(n-1)
#print("Factorial of ",num,"is",fact(num))

#factorial using loops
result = 1
for i in range(num,0,-1):
  result = result*i

print("Factorial of",num,"is : ",result)
