def checkdivisible(no1):
  if no1%3==0 and no1%5==0  :
    return True
  else:
    return False
  
def main():
  Value1=int(input("Enter number"))
  Ret=checkdivisible(Value1)
  print("Number is divisible by 3 :",Ret)

if __name__=="__main__":
 main()
