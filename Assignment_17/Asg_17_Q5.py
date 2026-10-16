def CheckPrime(no1):
   if no1<=1:
     return "Number is not prime"
   
   for i in range(2,no1):
     if no1%i!=0:
       return "Number is prime"
     else:
       return "Number is not prime"
     
def main():
 No1=int(input("Enter 1st number "))
 print(CheckPrime(No1))
if __name__=="__main__":
 main()
