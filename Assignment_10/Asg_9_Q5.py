def Getodd (val1):
 ret=list()
 val=""
 for x in range(val1+1):
  if x==0:
    pass
  else:
   if x%2!=0:
      val=val+" "+str(x)

      #ret.append(val)
 
 return val[3:]
 

def main():
  no1=int(input("Enter number to get Odd list  "))
  print("Odd numbers list :",Getodd(no1))
  
  #10=2,4,6,8,10


if __name__=="__main__":
 main()
