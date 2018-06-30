from models import *
from flask import Flask, jsonify, request, url_for, render_template, redirect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

import json

engine = create_engine('sqlite:///books.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)


# route: homepage
@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
  books = session.query(Book).all()
  genres = session.query(Genre).all()
  authors = session.query(Author).all()
  return render_template('index.html', books = books, genres = genres, authors = authors)


# route: login
@app.route('/login')
def login():
  pass

# route: logout
def logout():
  pass

# route: category list
@app.route('/catalog')
def catalog():
  return "Catalog!"


# route: category results
@app.route('/catalog/category/<category>')
def catalog_category(category):
  genre = session.query(Genre).filter_by(type = category).one()
  return render_template('category.html', genre = genre)


# route: category (books)
@app.route('/catalog/books/')
@app.route('/catalog/book/')
def catalog_books():
  books = session.query(Book).all()
  return render_template('catalog_books.html', books = books)


# route: category (genres)
@app.route('/catalog/genres/')
@app.route('/catalog/genre/')
def catalog_genres():
  genres = session.query(Genre).all()
  return render_template('catalog_genre.html', genres = genres)


# route: item (book)
@app.route('/catalog/book/<int:id>')
def catalog_book(id):
  book = session.query(Book).filter_by(id = id).one()
  return render_template('book.html', book = book)


# route: create item (book)
@app.route('/catalog/book/new', methods=['GET', 'POST'])
def new_book():
  if request.method == "POST":
    new_book = Book(title=request.form['title'], cover=request.form['cover'], description=request.form['description'])
    session.add(new_book)
    session.commit()
    return redirect(url_for('catalog_books'))
  else:
    return render_template('book_create.html')


# route: edit item (book)
@app.route('/catalog/book/<int:id>/edit', methods=['GET', 'POST'])
def edit_book(id):
  book = session.query(Book).filter_by(id = id).one()
  if request.method == 'POST':
    if request.form['title']:
      book.title = request.form['title']
    if request.form['cover']:
      book.cover = request.form['cover']
    if request.form['description']:
      book.description = request.form['description']
    session.add(book)
    session.commit()
    return redirect(url_for('catalog_book', id = book.id))
  else:
    return render_template('book_edit.html', book = book)


# route: delete item (book)
@app.route('/catalog/book/<int:id>/delete', methods=['GET', 'POST'])
def delete_book(id):
  book = session.query(Book).filter_by(id = id).one()
  if request.method == 'POST':
    session.delete(book)
    session.commit()
    return redirect(url_for('catalog_book'), id = book.id)
  else:
    return render_template('book_delete.html', book = book)


# route: item (genre)
@app.route('/catalog/genre/<int:id>')
def catalog_genre(id):
  genre = session.query(Genre).filter_by(id = id).one()
  return render_template('genre.html', genre = genre)


# route: create item (genre)
@app.route('/catalog/genre/new', methods=['GET', 'POST'])
def new_genre():
  pass


# route: edit item (genre)
@app.route('/catalog/genre/<int:id>/edit', methods=['GET', 'POST'])
def edit_genre(id):
  pass


# route: delete item (genre)
@app.route('/catalog/genre/<int:id>/delete', methods=['GET', 'POST'])
def delete_genre(id):
  genre = session.query(Genre).filter_by(id = id).one()
  if request.method == 'POST':
    session.delete(genre)
    session.commit()
    return redirect(url_for('catalog_genre'), id = id)
  else:
    return render_template('genre_delete.html', genre = genre)



if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0', port=8000, threaded = False)