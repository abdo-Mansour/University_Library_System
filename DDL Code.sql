use librarySystem;

CREATE DATABASE library;

CREATE TABLE book(
  bookID int primary key identity,
  title nvarchar(500) not null ,
  pageCount int check (pageCount > 0),
  ISBN nvarchar(50) unique,
  language nvarchar(500),
  description nvarchar(3500),
  publisher nvarchar(500),
  minimumAgeToRead int check (minimumAgeToRead >= 1),
  publicationYear smallint
);

CREATE TABLE bookGenre(
    bookID int not null ,
    genre nvarchar(50) not null ,
    primary key (bookID, genre),
    foreign key (bookID) references book(bookID)
)

CREATE TABLE author(
    authorID int primary key identity,
    firstName nvarchar(500) not null ,
    thirdName nvarchar(500) not null ,
)

CREATE TABLE authorsOfBook(
    bookID int not null ,
    authorID int not null ,
    primary key (bookID,authorID),
    foreign key (bookID) references book(bookID),
    foreign key (authorID) references author(authorID)
)

CREATE TABLE location(
    locationID int primary key identity,
    floor smallint,
    section nvarchar(500),
    shelfNumber int check (shelfNumber > 0)
)

CREATE TABLE account(
    email nvarchar(200) primary key not null,
    passwordHash nvarchar(500),
)

CREATE TABLE person(
    personID int primary key identity,
    firstName nvarchar(500) not null ,
    lastName nvarchar(500) not null,
    phoneNumber nvarchar(15) unique,
    dateOfBirth date,
    sex smallint,
    isAdmin smallint
)

CREATE TABLE emailOf(
    personID int not null,
    email nvarchar(200) not null,
    primary key (personID,email),
    foreign key (email) references account (email),
    foreign key (personID) references person (personID),
)

CREATE TABLE bookCopy(
    copyID int not null,
    bookID int not null,
    borrowerID int,
    locationID int,
    Condition nvarchar(500),
    isReturned smallint,
    borrowedDate date,
    periodInDays smallint,

    primary key (copyID, bookID),
    foreign key (borrowerID) references person (personID),
    foreign key (locationID) references location (locationID)
)
