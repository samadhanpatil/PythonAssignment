def Multitable(val1):
 ret1=""
 for x in range(11):
   #if x!=0:
   Ret=x*val1
   #print("Multiplication of number :",Ret)
   ret1=ret1+" "+str(Ret)
 var1=ret1[3:]
   
 print("Multiplication of list number :",var1) 

def main():
  no1=int(input("Enter number of mutiplication table "))
  Multitable(no1)


if __name__=="__main__":
 main()
