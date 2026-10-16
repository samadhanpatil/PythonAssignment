def GetResult(no1):

  if no1>=75:
    return "Distinction"
  elif no1>=60 and no1<75:
    return "First Class"
  elif no1>=50 and no1<60:
    return "Second Class"
  elif no1<50:
    return "Fail"
   
def main():
  no1=int(input("Enter marks of student "))
   
  print(f"Result of Student is : {GetResult(no1)}")


if __name__=="__main__":
 main()
