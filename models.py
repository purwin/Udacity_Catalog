from sqlalchemy import Column,Integer,String,Table,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    library = relationship('Book', secondary='library', backref='user_library', lazy='dynamic')
    wishlist = relationship('Book', secondary='library', backref='user_wishlist', lazy='dynamic')


class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True)
    title = Column(String(80))
    cover = Column(String)
    description = Column(String)
    authors = relationship('Author', secondary='book_author', backref='books', lazy='dynamic')
    genres = relationship('Genre', secondary='book_genre', backref='books', lazy='dynamic')


class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True)
    last_name = Column(String(80))
    first_name = Column(String(80))
    # full_name
    bio = Column(String)


class Genre(Base):
    __tablename__ = "genre"
    id = Column(Integer, primary_key=True)
    type = Column(String(80))


Table('book_author', Base.metadata,
      Column('book_id', Integer, ForeignKey('book.id')),
      Column('author_id', Integer, ForeignKey('author.id'))
     )


Table('book_genre', Base.metadata,
      Column('book_id', Integer, ForeignKey('book.id')),
      Column('genre_id', Integer, ForeignKey('genre.id'))
     )


Table('library', Base.metadata,
      Column('user_id', Integer, ForeignKey('user.id')),
      Column('book_id', Integer, ForeignKey('book.id'))
     )

Table('wishlist', Base.metadata,
      Column('user_id', Integer, ForeignKey('user.id')),
      Column('book_id', Integer, ForeignKey('book.id'))
     )


engine = create_engine('sqlite:///books.db')

Base.metadata.create_all(engine)