ret=lambda no1:True if no1%5==0 else False
def main():
  no1=int(input("Enter number "))
   
  print("Number is Divisible by 5 :- ",ret(no1) )


if __name__=="__main__":
 main()
