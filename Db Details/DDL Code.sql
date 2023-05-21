use librarySystem;

create table book(
  bookID int primary key identity,
  title nvarchar(500) not null ,
  pageCount int check (pageCount > 0),
  ISBN nvarchar(50) unique,
  language nvarchar(500),
  description nvarchar(3500),
  publisher nvarchar(500),
  minimumAgeToRead int check (minimumAgeToRead >= 1),
  publicationYear smallint,
  locationID int,
);

create table bookGenre(
    bookID int not null ,
    genre nvarchar(50) not null ,
    primary key (bookID, genre),
    foreign key (bookID) references book(bookID)
)

create table author(
    authorID int primary key identity,
    firstName nvarchar(500) not null ,
    lastName nvarchar(500) not null ,
)

create table authorsOfBook(
    bookID int not null ,
    authorID int not null ,
    primary key (bookID,authorID),
    foreign key (bookID) references book(bookID),
    foreign key (authorID) references author(authorID)
)

create table location(
    locationID int primary key identity,
    floor smallint,
    section nvarchar(500),
    shelfNumber int check (shelfNumber > 0)
)


create table person(
    personID int primary key identity,
    email nvarchar(200) not null,
    passwordHash nvarchar(500) not null,
    firstName nvarchar(500) not null ,
    lastName nvarchar(500) not null,
    phoneNumber nvarchar(15) unique,
    dateOfBirth date,
    sex smallint,
    isAdmin smallint,
)

create table bookCopy(
    copyID int not null,
    bookID int not null,
    borrowerID int,
    locationID int,
    physicalCondition nvarchar(500),
    isReturned smallint,
    borrowedDate date,
    periodInDays smallint,

    primary key (copyID, bookID),
    foreign key (bookID) references book (bookID)
    -- the following two lines are probably not good for our use
--     foreign key (borrowerID) references person (personID),
--     foreign key (locationID) references location (locationID)
)
