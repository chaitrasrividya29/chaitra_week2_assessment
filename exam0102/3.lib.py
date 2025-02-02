class book():
    def __init__ (self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
    def display(self):
        print("title of the book",self.title)
        print("author of the book",self.author)
        print("isbn of the book",self.isbn)

b=book("somthing i never told you","Shravya Bhinder",123456)
b.display()