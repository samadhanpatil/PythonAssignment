import threading,time

def EvenFactor(No1):
   print("Inside EvenFactor thread :",threading.get_ident())
   dolist=list()
   for i in range(1,No1+1):
    if No1%i==0:
      if i % 2 == 0:
       dolist.append(i)

   return dolist


def OddFactor(No1):
   print("Inside OddFactor thread :",threading.get_ident())
   dolist=list()
   for i in range(1,No1+1):
    if No1%i==0:
      if i % 2 == 1:
       dolist.append(i)

   return dolist
def main():
  print("Inside main thread :",threading.get_ident())

  start_time=time.perf_counter() 
  T1=threading.Thread(target=EvenFactor,args=(12,))
  T1.start()
  
  T2=threading.Thread(target=OddFactor,args=(12,))
  T2.start()
  
  T1.join()
  T1.join()
  end_time=time.perf_counter()
  print(f"Time required is {end_time-start_time:.4f}")

  print(f"Results is Even Factor {EvenFactor(12)}")
  print(f"Results is odd Factor {OddFactor(12)}")
if __name__=="__main__":
    main()