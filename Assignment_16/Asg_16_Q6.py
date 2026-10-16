def checkno(no1):
 if no1>1:
  return "Positive Nunber"
 elif no1<0:
  return "Negative Nunber"
 elif no1==0:
  return "Number is Zero"

def main():
 no1=int(input("Enter Number to check "))
 print("Enter value is ", checkno(no1))


if __name__=="__main__":
 main()
