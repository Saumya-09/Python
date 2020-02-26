class BookStore:
    NoOfBooks = 0

    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        self.NoOfBooks = self.NoOfBooks + 1
    def Display(self):
        print(self.Name+" by "+self.Author)
        print("No of books: ",self.NoOfBooks)

if __name__=='__main__':
    obj1 = BookStore("Linux System Programing", "Robert Love")
    obj1.Display()

    obj2 = BookStore("C Programing", "Dennis Ritchie")
    obj2.Display()
