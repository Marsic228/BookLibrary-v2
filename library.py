class Book:
    def __init__(self, title, author, year, is_read):
        self.title = title
        self.author = author
        self.year = year
        self.is_read = is_read

    def to_dict (self):
        return {"title" : self.title, "author" : self.author, "year" : self.year, "is_read" : self.is_read}
    
    def status (self):
        
    
