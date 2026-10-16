def PrintRevSeries(val1):
 ret=list()
 for i in range(val1,0,-1):
  #print(f"reverse number list is {i}")
  ret.append(str(i))

 return ' '.join(ret)

def main():
  no1=int(input("Enter First number "))
   
  print("Reverse series is :- ", PrintRevSeries(no1))



if __name__=="__main__":
 main()


