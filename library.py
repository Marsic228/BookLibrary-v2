import json

class Book:
    def __init__(self, title, author, year, is_read):
        self.title = title
        self.author = author
        self.year = year
        self.is_read = is_read

    def to_dict (self):
        return {"title" : self.title, "author" : self.author, "year" : self.year, "is_read" : self.is_read}
    
    def status (self):
        if self.is_read == True:
            return "✓ Read"
        else:
            return "✗ Not read"
    
def load_books (filename):
    result = []
    try:
        with open(filename) as file:
            loaded = json.load(file) 
    except FileNotFoundError:
        return []
    
    for i in loaded:
        book = Book(i["title"], i["author"], i["year"], i["is_read"])
        result.append(book)
    return result
  
def save_books(filename, books):
    result = []
    for i in books:
        result.append(i.to_dict())
    with open(filename, "w") as file:
        json.dump(result, file)

def add_book (books):
    title = input("Book title: ")
    author = input("Book author: ")
    year = int(input("Book year: "))
    answer = input("Read? (y/n): ")
    is_read = answer == "y"

    result = Book(title, author, year, is_read)
    books.append(result)
    print("Book added!")


def main():
    filename = "Book Library v2.json"
    books = load_books (filename)
    print("Book Library v2")
    add_book(books)
    save_books(filename, books)


main()