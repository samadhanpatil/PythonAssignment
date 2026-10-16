def CheckFactor(val1):
  factors=[]

  for i in range(1,val1+1):
     if val1%i ==0:
       factors.append(str(i))

  return ' '.join(factors)

def main():
  no1=int(input("Enter numbers to get factors "))
  print("factors of numbers are :- ", CheckFactor(no1))


if __name__=="__main__":
 main()
