import Arithmetic 
#Add,Sub,Mult,Div  

def main():
 No1=int(input("Enter 1st number "))
 No2=int(input("Enter 2nd Number "))
 print(f"Addition of number is {Arithmetic.Add(No1,No2)}")
 print(f"Substraction of number is {Arithmetic.Sub(No1,No2)}")
 print(f"Mult of number is {Arithmetic.Mult(No1,No2)}")
 print(f"Divison of number is {Arithmetic.Div(No1,No2)}")

if __name__=="__main__":
 main()
