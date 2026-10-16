class Demo:
  #Class variables
  Value1=10

  def __init__(self,A,B):  #Constructor Method
    self.No1=A
    self.No2=B


  def fun(self):
    print("Inside instance method")
    print(f"Inside Gun Method {self.No1}")
    print(f"Inside Gun Method {self.No2}")

  def gun(self):
    print("Inside Another Instance Method")
    print(f"Inside Gun Method {self.No1}")
    print(f"Inside Gun Method {self.No2}")


Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)

Obj1.fun()
Obj2.fun()
Obj1.gun()
Obj2.gun()