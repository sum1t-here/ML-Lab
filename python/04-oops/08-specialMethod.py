class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    ## __len__(self), __repr__, __add__
    def __len__(self):
        return self.pages
    
    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.pages})"
    

book1 = Book("Rich dad poor dad", "Robert Kiyosaki", 100)


# Test special methods

print(book1) # Rich dad poor dad by Robert Kiyosaki
print(len(book1)) # 100
print(repr(book1)) # Book(Rich dad poor dad, Robert Kiyosaki, 100)