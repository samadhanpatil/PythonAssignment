import os
def countlines(Fname):

  if (os.path.exists(Fname)):
    obj=open(Fname,'r')
    lines = obj.read()
     
    return lines
    obj.close()
    
  
def main():
 Filename=input('Enter File Name to Process')
 Ret=countlines(Filename)
 print(f"Total line in file are :{Ret} ")

if __name__=='__main__':
  main()