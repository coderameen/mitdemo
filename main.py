#Library Management System
class LibraryManagementSystem:
    #constructor
    def __init__(self):
        self.books = []
        
    def add_book(self,title,author,copies):
        book = {
            "title":title,
            "author":author,
            "copies":copies,
            "available_copies":copies
        }
        self.books.append(book)
        print(f"{title} book has been added to library!!!")
    
    def display_book(self):
        if self.books:
            print("BOOK Details")
            for book in self.books:
                print(f"Book Title: {book['title']} | Book Author: {book['author']} | Available copies: {book['available_copies']}")
        else:
            print("No books available")
    #helper function to find book(to check title book is present or not)
    def find_book(self, title):
        for book in self.books:
            if book['title'] == title:
                return book
        return None
    def barrow_book(self,title):
        book = self.find_book(title)
        if book is not None:
            if book['available_copies'] <= book['copies']:
                book['available_copies'] -= 1
                print(f"{title} book has been barrowed successfully!!")
        else:
            print(f"The {title} book is not present in library!!")
            
    def return_book(self,title):
        book = self.find_book(title)
        if book is not None:
            if book['available_copies'] < book['copies']:
                book['available_copies'] += 1
                print(f"{title} book has been returned successfully!!")
        else:
            print(f"The {title} book is not belongs to library!!")
        
            
s = LibraryManagementSystem()
s.add_book('Alogrithms','Alen',5)
s.add_book('Masterpython','bob',10)
# s.display_book()
s.barrow_book('Alogrithms')
s.display_book()