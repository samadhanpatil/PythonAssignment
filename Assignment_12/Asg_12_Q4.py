def PrintSeries(val1):
 series=list()
 for i in range(1,val1+1):
  series.append(str(i))

 return ' '.join(series)

def main():
  no1=int(input("Enter First number "))
   
  print("Addition of numbers are :- ", PrintSeries(no1))



if __name__=="__main__":
 main()
