import threading,time

Minelement=lambda a:max(a)
Maxelement=lambda a:min(a)

def main():
  data=list()
  No1=int(input("Enter number of Elements "))

  for i in range(No1):
    No2=int(input(f"Enter element for list  "))
    data.append(No2)
  # data=[2,34,5,67,89]
  print("Parent thread starts here",threading.get_ident())

  start_time=time.perf_counter() 
  T1=threading.Thread(target=Minelement,args=(data,))
  T1.start()

  T1=threading.Thread(target=Maxelement,args=(data,))
  T1.start()

  T1.join()
  T1.join()
  
  end_time=time.perf_counter()
  print(f"Time required is {end_time-start_time:.4f}")

  # print(f"Result Min",Minelement(data))
  # print(f"Result Max ",Maxelement(data))

if __name__=="__main__":
  main()


 