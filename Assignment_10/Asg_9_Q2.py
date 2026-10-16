def GetNaturalNoSum(val1):
 sum=0
 for x in range(val1+1):
   sum=sum+x
 return sum
 

def main():
  no1=int(input("Enter number of mutiplication table "))
  print("Sum of natural numbers is : ",GetNaturalNoSum(no1))
  
  #1,2,3,4,5=15


if __name__=="__main__":
 main()
