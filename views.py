from models import *
from flask import Flask, jsonify, request, url_for, render_template
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
    return render_template('index.html')


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
    pass


# route: category results
@app.route('/catalog/category/<category>')
def catalog_category(category):
    genre = session.query(Genre).filter_by(type = category).one()
    return render_template('category.html', genre = genre)


# route: item (book)
@app.route('/catalog/book/<int:id>')
def catalog_item(id):
    book = session.query(Book).filter_by(id = id).one()
    return render_template('book.html', book = book)


# route: create item (book)
@app.route('/catalog/book/<int:id>/new', methods=['GET', 'POST'])
def new_item(id):
    return render_template('book_new.html')


# route: edit item (book)
@app.route('/catalog/book/<int:id>/edit', methods=['GET', 'POST'])
def edit_item(id):
    return render_template('book_edit.html')


# route: delete item (book)
@app.route('/catalog/book/<int:id>/delete', methods=['GET', 'POST'])
def delete_item(id):
    return render_template('book_delete.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000, threaded = False)