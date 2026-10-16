import os
def countlines(Fname):

  if (os.path.exists(Fname)):
    obj=open(Fname,'r')
    lines = obj.read()
    words=lines.split()
    
    obj.close()
    
  return len(words)
def main():
 Filename=input('Enter File Name to Process')
 Ret=countlines(Filename)
 print(f"Total line in file are :{Ret} ")

if __name__=='__main__':
  main()