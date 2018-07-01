from models import *
from flask import Flask, jsonify, request, url_for, render_template, redirect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)


CLIENT_ID = json.loads(open('client_secret.json', 'r').read())['web']['client_id']
APPLICATION_NAME = 'UD Catalog Project'

engine = create_engine('sqlite:///books.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# route: homepage
@app.route('/')
@app.route('/home')
@app.route('/index')
@app.route('/catalog')
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
  return render_template('catalog_genres.html', genres = genres)


# route: category (authors)
@app.route('/catalog/authors/')
@app.route('/catalog/author/')
def catalog_authors():
  authors = session.query(Author).all()
  return render_template('catalog_authors.html', authors = authors)


# route: item (book)
@app.route('/catalog/book/<int:id>')
def catalog_book(id):
  book = session.query(Book).filter_by(id = id).one()
  return render_template('book.html', book = book)


# route: create item (book)
@app.route('/catalog/book/create', methods=['GET', 'POST'])
def create_book():
  if request.method == "POST":
    new_book = Book(title=request.form['title'], cover=request.form['cover'], description=request.form['description'])
    session.add(new_book)
    for author_id in request.form.getlist('author'):
      append_author = session.query(Author).filter_by(id=author_id).one()
      new_book.authors.append(append_author)
    for genre_id in request.form.getlist('genre'):
      append_genre = session.query(Genre).filter_by(id=genre_id).one()
      new_book.genres.append(append_genre)
    session.commit()
    return redirect(url_for('catalog_books'))
  else:
    authors = session.query(Author).all()
    genres = session.query(Genre).all()
    return render_template('book_create.html', authors = authors, genres = genres)


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
    return redirect(url_for('catalog_books'))
  else:
    return render_template('book_delete.html', book = book)


# route: item (genre)
@app.route('/catalog/genre/<int:id>')
def catalog_genre(id):
  genre = session.query(Genre).filter_by(id = id).one()
  return render_template('genre.html', genre = genre)


# route: create item (genre)
@app.route('/catalog/genre/create', methods=['GET', 'POST'])
def create_genre():
  if request.method == "POST":
    new_genre = Genre(type=request.form['type'])
    session.add(new_genre)
    for book_id in request.form.getlist('book'):
      append_book = session.query(Book).filter_by(id=book_id).one()
      new_genre.books.append(append_book)
    session.commit()
    return redirect(url_for('catalog_genres'))
  else:
    books = session.query(Book).all()
    return render_template('genre_create.html', books = books)


# route: edit item (genre)
@app.route('/catalog/genre/<int:id>/edit', methods=['GET', 'POST'])
def edit_genre(id):
  genre = session.query(Genre).filter_by(id = id).one()
  if request.method == 'POST':
    if request.form['type']:
      genre.type = request.form['type']
    session.add(genre)
    session.commit()
    return redirect(url_for('catalog_genre', id = genre.id))
  else:
    return render_template('genre_edit.html', genre = genre)


# route: delete item (genre)
@app.route('/catalog/genre/<int:id>/delete', methods=['GET', 'POST'])
def delete_genre(id):
  genre = session.query(Genre).filter_by(id = id).one()
  if request.method == 'POST':
    session.delete(genre)
    session.commit()
    return redirect(url_for('catalog_genres'))
  else:
    return render_template('genre_delete.html', genre = genre)


# route: item (author)
@app.route('/catalog/author/<int:id>')
def catalog_author(id):
  author = session.query(Author).filter_by(id = id).one()
  return render_template('author.html', author = author)


# route: create item (author)
@app.route('/catalog/author/create', methods=['GET', 'POST'])
def create_author():
  if request.method == "POST":
    new_author = Author(first_name=request.form['first_name'], last_name=request.form['last_name'], bio=request.form['bio'])
    session.add(new_author)
    for book_id in request.form.getlist('book'):
      append_book = session.query(Book).filter_by(id=book_id).one()
      new_author.books.append(append_book)
    session.commit()
    return redirect(url_for('catalog_authors'))
  else:
    books = session.query(Book).all()
    return render_template('author_create.html', books = books)


# route: edit item (author)
@app.route('/catalog/author/<int:id>/edit', methods=['GET', 'POST'])
def edit_author(id):
  author = session.query(Author).filter_by(id = id).one()
  if request.method == 'POST':
    if request.form['first_name']:
      author.first_name = request.form['first_name']
    if request.form['last_name']:
      author.last_name = request.form['last_name']
    if request.form['bio']:
      author.bio = request.form['bio']
    session.add(author)
    session.commit()
    return redirect(url_for('catalog_author', id = author.id))
  else:
    return render_template('author_edit.html', author = author)


# route: delete item (author)
@app.route('/catalog/author/<int:id>/delete', methods=['GET', 'POST'])
def delete_author(id):
  author = session.query(Author).filter_by(id = id).one()
  if request.method == 'POST':
    session.delete(author)
    session.commit()
    return redirect(url_for('catalog_authors'))
  else:
    return render_template('author_delete.html', author = author)



if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0', port=8000, threaded = False)