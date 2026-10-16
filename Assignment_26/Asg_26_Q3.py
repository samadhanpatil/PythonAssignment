class Arithmetic():
  # Value1=0
  # Value2=0

  def __init__(self):
    Value1=0
    Value2=0
    
  def Accept(self):
    No1=int(input("Enter 1st Number"))
    No2=int(input("Enter Second Number"))
    self.Value1=No1
    self.Value2=No2
    print(f"Values Enter are {No1} and {No2}")

  def Addition(self):
    return self.Value1+self.Value2
  
  def Subtraction(self):
    return self.Value1-self.Value2
  
  def Multiplication(self):
    return self.Value1*self.Value2
  
  def Division(self):
    return self.Value1/self.Value2

Obj1=Arithmetic()
Obj1.Accept()
Addition_Result=Obj1.Addition()
print(f"Result of Addition is {Addition_Result}")
Subtraction_Result=Obj1.Subtraction()
print(f"Result of Subtraction is {Subtraction_Result}")
Multiplication_Result=Obj1.Multiplication()
print(f"Result of Multiplication is {Multiplication_Result}")
Division_Result=Obj1.Division()
print(f"Result of Division is {Division_Result}")


Obj2=Arithmetic()
Obj2.Accept()
Addition_Result=Obj2.Addition()
print(f"Result of Addition is {Addition_Result}")
Subtraction_Result=Obj2.Subtraction()
print(f"Result of Subtraction is {Subtraction_Result}")
Multiplication_Result=Obj2.Multiplication()
print(f"Result of Multiplication is {Multiplication_Result}")
Division_Result=Obj2.Division()
print(f"Result of Division is {Division_Result}")