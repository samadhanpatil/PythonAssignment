def ChkGreater(no1,no2):
 if no1>no2:
  print("first number is greater then second",no1)
 else:
  print("Second number is greater then First",no2)
  
def main():
  Value1=int(input("Enter first number"))
  Value2=int(input("Enter second number"))
  ChkGreater(Value1,Value2)


if __name__=="__main__":
 main()
