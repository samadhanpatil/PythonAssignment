def Addition(val1,val2):
 return val1+val2

def Substract(val1,val2):
 return val1-val2

def Mult(val1,val2):
 return val1*val2

def Dev(val1,val2):
 return val1/val2


def main():
  no1=int(input("Enter First number "))
  no2=int(input("Enter Second number "))
  print("Addition of numbers are :- ", Addition(no1,no2))
  print("Substraction of numbers are :- ", Substract(no1,no2))
  print("Multiplication of numbers are :- ", Mult(no1,no2))
  print("Divison of numbers are :- ", Dev(no1,no2))


if __name__=="__main__":
 main()
