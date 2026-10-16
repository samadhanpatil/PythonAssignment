class BookStore():
  NoOfBooks=0

  def __init__(self,Name,Author):
    self.name = Name
    self.author = Author

  def Display(self):
    BookStore.NoOfBooks=BookStore.NoOfBooks+1
    print(f"{self.name} by {self.author}. No of books: {BookStore.NoOfBooks}")

Obj1 = BookStore("Linux System Programming", "Robert Love")
Obj1.Display()

Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display() # C Programming by Dennis Ritchie. No of books: 2

Obj2 = BookStore("Java Programming", "Ram AA")
Obj2.Display() # Java Programming by Ram AA. No of books: 2