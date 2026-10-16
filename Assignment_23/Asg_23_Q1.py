from multiprocessing import Pool
import time
import os

def GetEvenNo(no):
  print(f"PID of Main {os.getpid()} PPID of Parent is {os.getppid()}")
  sumno1=0
  for i in range(1,no+1):
    if i%2==0:
     sumno1=sumno1+i
  return sumno1
def main():

  data=[1000000,2000000,3000000,4000000]
  print(f"Pass data list is {data}")
  # ret=square(data)
  print(f"PID of Main {os.getpid()} PPID of Parent is {os.getppid()}")
  
  start_time=time.perf_counter() 
  with Pool() as pool:
    ret=pool.map(GetEvenNo,data)
 
  print(f"results using pool is {ret}")
  # end_time=time.perf_counter()
  # print(f"Time required is {end_time-start_time:.4f}")

if __name__=="__main__":
  main()


 