import threading,time

def EvenList (lst):
   print("Inside EvenFactor thread :",threading.get_ident())
   dolist=list()
   Sumno=0
   for i in range(len(lst)):
     if lst[i] % 2 == 0:
      dolist.append(lst[i])
      Sumno=Sumno+lst[i]

   print(f"Even list is ",dolist)
   print(f"Sum of Even list is ",Sumno)
   return Sumno


def OddList(lst):
   print("Inside OddFactor thread :",threading.get_ident())
   dolist=list()
   Sumno=0
   for i in range(len(lst)):
     if lst[i] % 2 != 0:
      dolist.append(lst[i])
      Sumno=Sumno+lst[i]
   print(f"odd list is ",dolist)
   print(f"Sum of Odd list is ",Sumno)
   return Sumno


def main():
  print("Inside main thread :",threading.get_ident())
  Data=[13,12,8,10,11,20]

  print("Original list is :",Data)
  start_time=time.perf_counter() 
  T1=threading.Thread(target=EvenList,args=(Data,))
  T1.start()
  
  T2=threading.Thread(target=OddList,args=(Data,))
  T2.start()
  
  T1.join()
  T1.join()
  end_time=time.perf_counter()
  print(f"Time required is {end_time-start_time:.4f}")

  # print(f"Results is Even list {EvenList(12)}")
  # print(f"Results is odd list {OddList(12)}")
if __name__=="__main__":
    main()