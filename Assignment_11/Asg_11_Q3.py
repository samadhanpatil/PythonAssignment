def countdigit(val1):
 cnt=0

 for i in val1:
  cnt=cnt+int(i)
 return cnt
def main():
  no1= (input("enter number"))

  print("Digit sum is ", countdigit(no1))


if __name__=="__main__":
 main()

