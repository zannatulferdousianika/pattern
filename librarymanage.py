class book:
    def __init__(self,book_name,author,is_borrowed):
        self.book_name = book_name
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"Book: {self.book_name} by {self.author} status: {status}")

    def book_borrowed(self):
        if not is_borrowed:
            self.is_borrowed = True
            return False
        return True

    def return_book(self):
        if self.is_borroewd:
            self.is_borrowed = False
            return True 
        return False

class patron:
    def __init__(self,name,patron_id,):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def __str__(self):
        print(f"Name: {self.name} , ID: {self.patron_id}, Book borrowed: {self.borrowed_books}")


    def add_book(self,book):
        self.borrowed_books.append(book)

    def remove_book(self , book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            return True 
        else:
            print("Book not found")
    
    def display_books(self):
        if not self.borrowed_books:
            print("No books in the library")
            return 

    
print("\n====Library Management====")
print("1. Display borrowed boooks ")
print("2. Add books ")
print("3. Remove books")
print("4. Exit ")
print("\n =====Thanks for using=====")

chose = input("Choose an option ")

if chose == '1':
    patron.display_books()
elif chose == '3':
    book1 = input("Enter book name")
    a1 = inpuut("Enter author name")
    if book1 in self.borrowed_books:
        patron.remove_book()

elif chose == '2':
    b2 = input("Enter book name")
    a2 = input("Enter book author")
    patron.add_book()

elif chose == '4':
    print("Thanks for using it")
     break

else:
    print("invalid index")

if __name__ == "__main__":
    book()
    patron()





