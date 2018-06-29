from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *

import random

engine = create_engine('sqlite:///books.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

book = {
    "title": "",
    "cover": "",
    "description": "",
    "authors": [
        {
            "last_name": "",
            "first_name": ""
        }
    ],
    "genres": [
    ""
    ]
}

great_gatsby = {
    "title": "The Great Gatsby",
    "cover": "",
    "description": "",
    "authors": [
        {
            "last_name": "Fitzgerald",
            "first_name": "F. Scott"
        }
    ],
    "genres": [
    "Literary Fiction"
    ]
}

book_catalog.append(great_gatsby)

cat_in_hat = {
    "title": "The Cat in the Hat",
    "cover": "",
    "description": "It’s a rainy day and Dick and Sally can’t find anything to do . . . until the Cat in the Hat unexpectedly appears and turns their dreary afternoon into a fun-filled extravaganza!",
    "authors": [
        {
            "last_name": "Suess",
            "first_name": "Dr."
        }
    ],
    "genres": [
    "Children’s Picture Books"
    ]
}
book_catalog.append(cat_in_hat)

def add_book(book):
    new_book = Book(title=book['title'], cover=book['cover'], description=book['description'])
    session.add(new_book)
    session.commit()

    for genre in book['genres']:
        try:
            genre_search = session.query(Genre).filter_by(type=genre).one()
        else:
          new_genre = Genre(type=genre)
          session.add(new_genre)
          session.commit()
          genre_search = session.query(Genre).filter_by(type=genre).one()
        new_book.genres.append(genre_search)

    for author in book['authors']:
        try:
            author_search = session.query(Author).filter_by(last_name=author['last_name'], first_name=author['first_name']).one()
        else:
          new_author = Author(last_name=author['last_name'], first_name=author['first_name'])
          session.add(new_author)
          session.commit()
          author_search = session.query(Author).filter_by(last_name=author['last_name'], first_name=author['first_name']).one()
        new_book.authors.add(author_search)

for book in book_catalog:
    add_book(book)

print "Added books and authors and genres, woot woot!"