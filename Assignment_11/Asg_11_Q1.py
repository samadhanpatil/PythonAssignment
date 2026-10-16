def isPrime(val1):
  if val1 <= 1:
      return False

  # Check divisibility from 2 to n-1
  for i in range(2,val1):
      if val1 % i == 0:
          return False

  return True
  
 

def main():
  no1=int(input("Enter number of to check prime or not "))
  print("Number is prime ", isPrime(no1))


if __name__=="__main__":
 main()
