use librarySystem;

INSERT INTO library.book (title, pageCount, ISBN, language, description, publisher, minimumAgeToRead, publicationYear)
VALUES
    ('The Great Gatsby', 218, '9780743273565', 'English', 'A novel by F. Scott Fitzgerald', 'Scribner', 14, 1925),
    ('To Kill a Mockingbird', 324, '9780061120084', 'English', 'A novel by Harper Lee', 'HarperCollins', 13, 1960),
    ('1984', 328, '9780451524935', 'English', 'A dystopian novel by George Orwell', 'Signet Classics', 16, 1949),
    ('Pride and Prejudice', 432, '9780141439518', 'English', 'A novel by Jane Austen', 'Penguin Classics', 15, 1813),
    ('The Hobbit', 310, '9780547928227', 'English', 'A fantasy novel by J.R.R. Tolkien', 'Mariner Books', 12, 1937),
    ('Harry Potter and the Sorcerer''s Stone', 320, '9780590353427', 'English', 'A fantasy novel by J.K. Rowling', 'Scholastic', 9, 1997),
    ('The Catcher in the Rye', 234, '9780316769174', 'English', 'A novel by J.D. Salinger', 'Little, Brown and Company', 16, 1951),
    ('The Alchemist', 208, '9780061122415', 'English', 'A novel by Paulo Coelho', 'HarperOne', 14, 1988),
    ('The Lord of the Rings', 1178, '9780618640157', 'English', 'A fantasy novel by J.R.R. Tolkien', 'Houghton Mifflin Harcourt', 14, 1954),
    ('The Chronicles of Narnia', 767, '9780066238500', 'English', 'A series of fantasy novels by C.S. Lewis', 'HarperCollins', 10, 1950);

INSERT INTO library.bookGenre (bookID, genre)
VALUES
    (1, 'Fiction'),
    (2, 'Classic'),
    (2, 'Coming-of-age'),
    (3, 'Dystopian'),
    (4, 'Romance'),
    (5, 'Fantasy'),
    (5, 'Adventure'),
    (6, 'Fantasy'),
    (6, 'Children'),
    (7, 'Fiction');

INSERT INTO library.author (firstName, lastName)
VALUES
    ('F. Scott', 'Fitzgerald'),
    ('Harper', 'Lee'),
    ('George', 'Orwell'),
    ('Jane', 'Austen'),
    ('J.R.R.', 'Tolkien'),
    ('J.K.', 'Rowling'),
    ('J.D.', 'Salinger'),
    ('Paulo', 'Coelho'),
    ('C.S.', 'Lewis'),
    ('Markus', 'Zusak');

INSERT INTO library.authorsOfBook (bookID, authorID)
VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 5),
    (10, 9);

INSERT INTO library.location (floor, section, shelfNumber)
VALUES
    (1, 'Fiction', 3),
    (2, 'Classics', 2),
    (3, 'Fantasy', 5),
    (2, 'Children', 1),
    (4, 'Mystery', 4),
    (1, 'Non-Fiction', 2),
    (3, 'Science Fiction', 3),
    (2, 'Biography', 1),
    (4, 'Romance', 5),
    (3, 'History', 4);

INSERT INTO library.person (email, passwordHash, firstName, lastName, phoneNumber, dateOfBirth, sex, isAdmin)
VALUES
    ('user1@example.com', 'password1', 'John', 'Doe', '1234567890', '1990-05-12', 1, 0),
    ('user2@example.com', 'password2', 'Jane', 'Smith', '9876543210', '1985-09-23', 0, 0),
    ('admin@example.com', 'adminpass', 'Admin', 'User', '5555555555', '1978-12-03', 1, 1),
    ('user3@example.com', 'password3', 'David', 'Johnson', '9999999999', '1998-07-01', 1, 0),
    ('user4@example.com', 'password4', 'Emily', 'Williams', '1111111111', '1992-03-18', 0, 0),
    ('user5@example.com', 'password5', 'Sarah', 'Brown', '2222222222', '1987-11-10', 0, 0),
    ('user6@example.com', 'password6', 'Michael', 'Davis', '3333333333', '1995-06-05', 1, 0),
    ('user7@example.com', 'password7', 'Jennifer', 'Anderson', '4444444444', '1991-09-15', 0, 0),
    ('user8@example.com', 'password8', 'Christopher', 'Martinez', '5533255555', '1999-02-27', 1, 0),
    ('user9@example.com', 'password9', 'Amanda', 'Thomas', '6666666666', '1993-04-20', 0, 0);

INSERT INTO library.bookCopy (copyID, bookID, borrowerID, locationID, physicalCondition, isReturned, borrowedDate, periodInDays)
VALUES
    (1, 1, NULL, 1, 'Good', 1, '2023-05-10', 14),
    (2, 2, 2, 2, 'Excellent', 0, '2023-04-25', 21),
    (3, 3, 3, 3, 'Fair', 0, '2023-05-01', 7),
    (4, 4, NULL, 4, 'Good', 1, '2023-05-15', 10),
    (5, 5, 5, 5, 'Very Good', 0, '2023-04-28', 14),
    (6, 6, 6, 6, 'Excellent', 0, '2023-05-02', 14),
    (7, 7, NULL, 7, 'Fair', 1, '2023-05-12', 14),
    (8, 8, 7, 8, 'Good', 0, '2023-05-03', 7),
    (9, 9, 8, 9, 'Excellent', 0, '2023-04-30', 21),
    (10, 10, NULL, 10, 'Very Good', 1, '2023-05-08', 14);