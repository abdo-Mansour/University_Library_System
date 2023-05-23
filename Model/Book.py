class Book:
    def __init__(self, Title=None, ISBN=None, PageCount=None, Language=None, Description=None, Publisher=None, MinAgeToRead=None, PublicationYear=None,BookID=None):
        self.BookID = BookID
        self.Title = Title
        self.ISBN = ISBN
        self.PageCount = PageCount
        self.Language = Language
        self.Description = Description
        self.Publisher = Publisher
        self.MinimumAgeToRead = MinAgeToRead
        self.PublicationYear = PublicationYear
        self.attributes = ['BookID', 'Title', 'PageCount',
                           'ISBN', 'Language', ' Description', 'Publisher', 'MinAgeToRead', 'PublicationYear']
