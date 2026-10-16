from multiprocessing import Pool
import time
import os
import math

def calculate_sum_loop(n):
    """Calculates the sum using a simple loop: O(N) time complexity."""
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i ** 5
    return total_sum

def main():
 print(f"PID of Main {os.getpid()} PPID of Parent is {os.getppid()}")
 start_time=time.perf_counter() 
#  data = [10000,20000,30000,40000]
 data = [5,7]
 with Pool() as pool:
    ret=pool.map(calculate_sum_loop,data)

 print(f"results using pool is {ret}")

 end_time=time.perf_counter()
 print(f"Time required is {end_time-start_time:.4f}")


if __name__=="__main__":
  main()


 