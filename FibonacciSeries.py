#FibonacciSeries

len=int(input("How many numbers to be printed in this series:"))
t1=0
t2=1
for i in range(len):
  print(t1,end=" ")
  t3=t1
  t1=t2
  t2=t1+t3
