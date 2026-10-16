ret=lambda no1,no2,no3:max(no1,no2,no3)
def main():
  no1=int(input("Enter first number "))
  no2=int(input("Enter second number "))
  no3=int(input("Enter Third number "))
  print("Largest of 3 number is :- ",ret(no1,no2,no3) )


if __name__=="__main__":
 main()
