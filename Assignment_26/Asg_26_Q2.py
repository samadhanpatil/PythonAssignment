class Circle():
  PI=3.14
  def __init__(self):
    self.Radius=0
    self.Area=0
    self.Circum=0

  def Accept(self):
   Rd=int(input("Enter Radius of Circle"))
   self.Radius=Rd

  def CalculateArea(self):
    return self.PI*(self.Radius**2)
  
  def CalculateCircumference(self):
    return 2*self.PI*self.Radius

  def display(self):
    """Instance method to display the final area."""
    area = self.CalculateArea()
    print(f"The area of the circle with radius {self.Radius} is: {area:.2f}")
    Circumference = self.CalculateCircumference()
    print(f"The area of the circle with radius {self.Radius} is: {area:.2f}")

Obj1=Circle()

Obj1.Accept() 
Ret2=Obj1.CalculateArea() 
Ret3=Obj1.CalculateCircumference()
print(f"Calculated Area is {Ret2}")
print(f"Calculated Circumference is {Ret3}")

Obj2=Circle()

Obj2.Accept() 
Ret2=Obj2.CalculateArea() 
Ret3=Obj2.CalculateCircumference()
print(f"Calculated Area is {Ret2}")
print(f"Calculated Circumference is {Ret3}")

 




# obj1=Circle()
# print(obj1.PI)