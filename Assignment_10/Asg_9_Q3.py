def GetFactorial(val1):
 sum=1
 for x in range(val1+1):
   if x==0:
      sum=sum*x+1
   else:
     sum=sum*x
 return sum
 

def main():
  no1=int(input("Enter number to get Factorial  "))
  print("Factorial of number is : ",GetFactorial(no1))
  
  #1,2,3,4,5=1*2*3*4*5


if __name__=="__main__":
 main()
