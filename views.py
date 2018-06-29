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
@app.route('/catalog/<category>')
def catalog_category(category):
    return render_template('category.html')


# route: item (book)
@app.route('/catalog/<int:id>')
def catalog_item(id):
    book = session.query(Book).filter_by(id = id).one()
    return render_template('item.html', book = book)


# route: create item (book)
@app.route('/catalog/<int:id>/new', methods=['GET', 'POST'])
def new_item(id):
    return render_template('item_new.html')


# route: edit item (book)
@app.route('/catalog/<int:id>/edit', methods=['GET', 'POST'])
def edit_item(id):
    return render_template('item_edit.html')


# route: delete item (book)
@app.route('/catalog/<int:id>/delete', methods=['GET', 'POST'])
def delete_item(id):
    return render_template('item_delete.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000, threaded = False)