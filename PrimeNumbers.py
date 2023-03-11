#PrimeNumbers

lower=int(input("Enter the lower interval : "))
upper=int(input("Enter the upper interval : "))
if lower>upper:
  print("Invalid Input.")
def isPrime(num):
  if num<2:
    return False
  for j in range(2,num//2+1):
    if num%j==0:
      return False
  return True
for i in range(lower,upper+1):
  if isPrime(i):
    print(i," is a Prime Number")
