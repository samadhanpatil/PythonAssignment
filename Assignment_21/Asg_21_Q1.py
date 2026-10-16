import threading,time

def isPrime(n):
    if (n<2):
        return False
    for i in range (2,n):
        if (n%i==0):
            return False
    return True

def checkprime(lst):
  print("Inside checkprime thread name :",threading.get_ident())
  print("Inside checkprime thread :",threading.current_thread().name)
  ret=list()
  for i in range(len(lst)):
     if isPrime(lst[i]):
        ret.append(lst[i])

  return ret

def NonPrime(lst):
  print("Inside NonPrime thread name :",threading.get_ident())
  print("Inside NonPrime thread :",threading.current_thread().name)
  NonPrime=list()
  for i in range(len(lst)):
     if not isPrime(lst[i]):
        NonPrime.append(lst[i])

  return NonPrime

def main():
  print("Parent thread starts here",threading.get_ident())
  data=[1,5,4,2,14]
  start_time=time.perf_counter() 
  T1=threading.Thread(target=checkprime,args=(data,))
  T1.start()

  T1=threading.Thread(target=NonPrime,args=(data,))
  T1.start()

  T1.join()
  T1.join()
  
  end_time=time.perf_counter()
  print(f"Time required is {end_time-start_time:.4f}")

if __name__=="__main__":
  main()


 