ret=lambda no1,no2:no1  if no1>no2 else no2
def main():
  no1=int(input("Enter First number "))
  no2=int(input("Enter Second number "))
  
  print("maximum number of two is :- ",ret(no1,no2) )


if __name__=="__main__":
 main()
