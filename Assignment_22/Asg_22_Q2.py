from multiprocessing import Pool
import time
import os

def square(no):
  print(f"PID of func all {no} {os.getpid()} PPID of Parent is {os.getppid()}")
  sumno1=1
  for i in range(1,no+1):
    sumno1=sumno1*i
    # sumno1=sumno1+sumno
  return sumno1
def main():

  data=[10,15,20,25]  #2 fact - 1*2 --2, 4-->1*2*3*4
  print(f"Pass data list is {data}")
  # ret=square(data)
  print(f"PID of Main {os.getpid()} PPID of Parent is {os.getppid()}")
  start_time=time.perf_counter() 
  with Pool() as pool:
    ret=pool.map(square,data)
 
  print(f"results using pool is {ret}")
  # end_time=time.perf_counter()
  # print(f"Time required is {end_time-start_time:.4f}")

if __name__=="__main__":
  main()


 