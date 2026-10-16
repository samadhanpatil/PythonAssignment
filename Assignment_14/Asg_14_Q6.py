ret=lambda no1:True if no1%2!=0 else False
def main():
  no1=int(input("Enter number "))
   
  print("Number is Odd :- ",ret(no1) )


if __name__=="__main__":
 main()
