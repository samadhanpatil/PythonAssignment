def countdigit(val1):
 cnt=1
 x=len(val1)
 for i in range(len(val1)):
   if i==0 :
     a=1
   else:
     a=i

     x=cnt+a
   
 return x
  
 

def main():
  no1= (input("enter number"))

  print("Number is prime ", countdigit(no1))


if __name__=="__main__":
 main()

