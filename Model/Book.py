class Book:
    def __init__(self, BookID=None, Title=None, ISBN=None, PageCount=None, Language=None, Description=None, Publisher=None, MinAgeToRead=None, PublicationYear=None):
        self.BookID = BookID
        self.Title = Title
        self.ISBN = ISBN
        self.PageCount = PageCount
        self.Language = Language
        self.Description = Description
        self.Publisher = Publisher
        self.MinAgeToRead = MinAgeToRead
        self.PublicationYear = PublicationYear
        self.attributes = ['BookID', 'Title', 'ISBN',
                           'PageCount', 'Language', ' Description', 'Publisher', 'MinAgeToRead', 'PublicationYear']
