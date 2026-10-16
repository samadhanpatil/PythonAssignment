import os
def countlines(SourceFileName,FindWord):

  if (os.path.exists(SourceFileName)):
    obj=open(SourceFileName,'r')
     
    lines = obj.read()

    if FindWord.lower() in  lines.lower():
      return True

    return False
  obj.close()
 
  
def main():
 SourceFileName=input('Enter Source File Name  to Process   ')
 FindWord=input('Enter Word to find in File to Process   ')
 Ret=countlines(SourceFileName,FindWord)
 print(f"{FindWord} is present in file : {Ret} ")

if __name__=='__main__':
  main()