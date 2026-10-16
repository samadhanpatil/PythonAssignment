import os
def countlines():

  if (os.path.exists("Demo.txt")):
    obj=open("Demo.txt",'r')
    lines = obj.readlines()
    obj.close()
    
  return len(lines)
def main():

 Ret=countlines()
 print(f"Total line in file are :{Ret} ")

if __name__=='__main__':
  main()