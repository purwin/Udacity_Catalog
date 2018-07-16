from models import *
from flask import Flask, jsonify, request, url_for, render_template, flash, redirect, make_response
from flask import session as login_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

import json
import random
import string
import sys
import os
import urllib


from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import requests

app = Flask(__name__)

engine = create_engine('sqlite:///books-02.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

g_client_id = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']
g_application_name = 'UD Catalog Project'


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
@app.route('/login/')
def login():
  state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
  login_session['state'] = state
  gh_params = {
               "scope": "user",
               "client_id": json.loads(open('gh_client_secrets.json', 'r').read())['web']['client_id'],
               "state": state
  }
  gh_url = 'https://github.com/login/oauth/authorize?{}'.format(urllib.urlencode(gh_params))
  return render_template('login.html', STATE = state, g_client_id = g_client_id, gh_url = gh_url)
  # gh_url = 'https://github.com/login/oauth/authorize?scope=user:email&client_id={}' + urllib.urlencode(gh_params)

  # client_id = json.loads(open('gh_client_secrets.json', 'r').read())['web']['client_id']
  # client_secret = json.loads(open('gh_client_secrets.json', 'r').read())['web']['client_secret']
  # redirect_uri = json.loads(open('gh_client_secrets.json', 'r').read())['web']['redirect_uri']
  # url = 'https://github.com/login/oauth/authorize?scope=user:email&client_id={}'.format(client_id)
  # h = httplib2.Http()
  # result = h.request(url, 'GET')[1]
  # print result


#route: gconnect
# Adapted from https://github.com/udacity/ud330
@app.route('/gconnect', methods=['POST'])
def gconnect():
  # Validate state token
  if request.args.get('state') != login_session['state']:
    response = make_response(json.dumps('Invalid state parameter.'), 401)
    response.headers['Content-Type'] = 'application/json'
    return response
  # Obtain authorization code
  code = request.data

  try:
    # Upgrade the authorization code into a credentials object
    oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
    oauth_flow.redirect_uri = 'postmessage'
    credentials = oauth_flow.step2_exchange(code)
  except FlowExchangeError:
    response = make_response(
      json.dumps('Failed to upgrade the authorization code.'), 401)
    response.headers['Content-Type'] = 'application/json'
    return response

  # Check that the access token is valid.
  access_token = credentials.access_token
  url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={}'.format(access_token))
  h = httplib2.Http()
  result = json.loads(h.request(url, 'GET')[1])
  # If there was an error in the access token info, abort.
  if result.get('error') is not None:
    response = make_response(json.dumps(result.get('error')), 500)
    response.headers['Content-Type'] = 'application/json'
    return response

  # Verify that the access token is used for the intended user.
  gplus_id = credentials.id_token['sub']
  if result['user_id'] != gplus_id:
    response = make_response(
        json.dumps("Token's user ID doesn't match given user ID."), 401)
    response.headers['Content-Type'] = 'application/json'
    return response

  # Verify that the access token is valid for this app.
  if result['issued_to'] != g_client_id:
    response = make_response(
        json.dumps("Token's client ID does not match app's."), 401)
    print "Token's client ID does not match app's."
    response.headers['Content-Type'] = 'application/json'
    return response

  stored_access_token = login_session.get('access_token')
  stored_gplus_id = login_session.get('gplus_id')
  if stored_access_token is not None and gplus_id == stored_gplus_id:
    response = make_response(json.dumps('Current user is already connected.'),
                             200)
    response.headers['Content-Type'] = 'application/json'
    return response

  # Store the access token in the session for later use.
  login_session['access_token'] = credentials.access_token
  login_session['gplus_id'] = gplus_id

  # Get user info
  userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
  params = {'access_token': credentials.access_token, 'alt': 'json'}
  answer = requests.get(userinfo_url, params=params)

  data = answer.json()

  login_session['username'] = data['name']
  login_session['picture'] = data['picture']
  login_session['email'] = data['email']

  user_id = getUserID(login_session['email'])
  if not user_id:
    user_id = createUser(login_session)
  login_session['user_id'] = user_id

  output = ''
  output += '<h1>Welcome, '
  output += login_session['username']
  output += '!</h1>'
  output += '<img src="'
  output += login_session['picture']
  output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
  flash("You are now logged in as {}".format(login_session['username']))
  print "done!"
  return output

# route: ghconnect
@app.route('/ghconnect', methods=['GET','POST'])
def ghconnect():
  if request.args.get('state') != login_session['state']:
    response = make_response(json.dumps('Invalid state parameter.'), 401)
    response.headers['Content-Type'] = 'application/json'
    return response

  # Receive code from GitHub
  code = request.args.get('code')
  print "GitHub code received: {}".format(code)
  state = request.args.get('state')
  print "state: {}".format(state)

  # Request access_token from GitHub with received code
  gh_url = 'https://github.com/login/oauth/access_token'
  gh_params = {
               "client_id": json.loads(open('gh_client_secrets.json', 'r').read())['web']['client_id'],
               "client_secret": json.loads(open('gh_client_secrets.json', 'r').read())['web']['client_secret'],
               "code": code,
               # "redirect_uri": 'http://localhost:8000/ghredirect',
               "state": state
  }
  gh_headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'application/json'}

  # POST to GitHub
  h = httplib2.Http()
  result, content = h.request(gh_url, 'POST', headers=gh_headers, body=urllib.urlencode(gh_params))
  print "RESULT STATUS: {}".format(result['status'])

  # Display error if no Success status
  if not result['status'] == '200':
    response = make_response(
        json.dumps('Code exchange failed with GitHub'), 401)
    response.headers['Content-Type'] = 'application/json'
    return response
  print "RESULT: {}".format(result)
  print "CONTENT: {}".format(content)

  # Store access token
  access_token = json.loads(content)['access_token']
  login_session['access_token'] = access_token
  print "CONTENT TOKEN: {}".format(access_token)

  # Get user data
  user_url = 'https://api.github.com/user'
  email_url = 'https://api.github.com/user/emails'
  header = {'Authorization': 'token {}'.format(access_token), 'Accept': 'application/json'}

  # Get user name
  h = httplib2.Http()
  result = h.request(user_url, 'GET', headers=header)[1]
  user_data = json.loads(result)
  login_session['provider'] = 'github'
  login_session['username'] = user_data['name']
  login_session['picture'] = user_data['avatar_url']

  # Get user email
  h = httplib2.Http()
  result = h.request(email_url, 'GET', headers=header)[1]
  email_data = json.loads(result)
  login_session['email'] = email_data[0]['email']

  # See if user exists, if it doesn't make a new one
  user_id = getUserID(login_session['email'])
  if not user_id:
      user_id = createUser(login_session)
  login_session['user_id'] = user_id

  output = ''
  output += '<h1>Welcome, '
  output += login_session['username']
  output += '!</h1>'
  output += '<img src="'
  output += login_session['picture']
  output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
  flash("you are now logged in as %s" % login_session['username'])
  return output


@app.route('/ghredirect', methods=['GET', 'POST'])
def ghredirect():
  if request.args.get('state') != login_session['state']:
    response = make_response(json.dumps('Invalid state parameter.'), 401)
    response.headers['Content-Type'] = 'application/json'
    return response
  access_token = request.args.get('access_token')
  print "ACCESS TOKEN: {}".format(access_token)


# User Helper Functions
# Adapted from https://github.com/udacity/ud330
def createUser(login_session):
  new_user = User(name = login_session['username'], email = login_session['email'], picture = login_session['picture'])
  session.add(new_user)
  session.commit()
  user = session.query(User).filter_by(email = login_session['email']).one()
  return user.id


def getUserInfo(id):
  user = session.query(User).filter_by(id = id).one()
  return user


def getUserID(email):
  try:
    user = session.query(User).filter_by(email = email).one()
    return user.id
  except:
    return None


#route: gdisconnect
# Adapted from https://github.com/udacity/ud330
@app.route('/gdisconnect')
def gdisconnect():
  access_token = login_session.get('access_token')
  if access_token is None:
    print 'Access Token is None'
    response = make_response(json.dumps('Current user not connected.'), 401)
    response.headers['Content-Type'] = 'application/json'
    return response
  print "Access! {}".format(access_token)
  print 'In gdisconnect access token is {}'.format(access_token)
  url = 'https://accounts.google.com/o/oauth2/revoke?token={}'.format(login_session['access_token'])
  h = httplib2.Http()
  result = h.request(url, 'GET')[0]
  print 'result is {}'.format(result)
  if result['status'] == '200':
    del login_session['access_token']
    del login_session['gplus_id']
    del login_session['username']
    del login_session['email']
    del login_session['picture']
    # response = make_response(json.dumps('Successfully disconnected.'), 200)
    # response.headers['Content-Type'] = 'application/json'
    # return response
    flash("You are now logged out")
    return redirect(url_for('index'))
  else:
    response = make_response(json.dumps('Failed to revoke token for given user.', 400))
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/account/')
def user_account():
  if 'username' not in login_session:
    return redirect(url_for('login'))
  else:
    user_id = getUserID(login_session['email'])
    user = getUserInfo(user_id)
    return render_template('user_account.html', user = user)


# route: add to library
@app.route('/catalog/book/<int:id>/library/add/', methods=['GET', 'POST'])
def add_library(id):
  if 'username' not in login_session:
    return redirect(url_for('login'))
  book = session.query(Book).filter_by(id = id).one()
  user_id = getUserID(login_session['email'])
  user = getUserInfo(user_id)
  if request.method == 'POST':
    user.library.append(book)
    session.commit()
    flash("{} is now in your library!".format(book.title))
    return redirect(url_for('catalog_books'))
  else:
    return render_template('library_add.html', book = book, user = user)


# route: remove from library
@app.route('/catalog/book/<int:id>/library/delete/', methods=['GET', 'POST'])
def delete_library(id):
  if 'username' not in login_session:
    return redirect(url_for('login'))
  book = session.query(Book).filter_by(id = id).one()
  user_id = getUserID(login_session['email'])
  user = getUserInfo(user_id)
  if request.method == 'POST':
    user.library.remove(book)
    session.commit()
    flash("{} has been removed from your library".format(book.title))
    return redirect(url_for('catalog_books'))
  else:
    return render_template('library_delete.html', book = book, user = user)


# route: add to wishlist
@app.route('/catalog/book/<int:id>/wishlist/add/', methods=['GET', 'POST'])
def add_wishlist(id):
  if 'username' not in login_session:
    return redirect(url_for('login'))
  book = session.query(Book).filter_by(id = id).one()
  user_id = getUserID(login_session['email'])
  user = getUserInfo(user_id)
  if request.method == 'POST':
    user.wishlist.append(book)
    session.commit()
    flash("{} is now in your wishlist!".format(book.title))
    return redirect(url_for('catalog_books'))
  else:
    return render_template('wishlist_add.html', book = book, user = user)


# route: remove from wishlist
@app.route('/catalog/book/<int:id>/wishlist/delete/', methods=['GET', 'POST'])
def delete_wishlist(id):
  if 'username' not in login_session:
    return redirect(url_for('login'))
  book = session.query(Book).filter_by(id = id).one()
  user_id = getUserID(login_session['email'])
  user = getUserInfo(user_id)
  if request.method == 'POST':
    user.wishlist.remove(book)
    session.commit()
    flash("{} has been removed from your wishlist".format(book.title))
    return redirect(url_for('catalog_books'))
  else:
    return render_template('wishlist_delete.html', book = book, user = user)


# route: category results
@app.route('/catalog/category/<category>')
def catalog_category(category):
  genre = session.query(Genre).filter_by(type = category).one()
  if 'username' in login_session:
    user_id = getUserID(login_session['email'])
    user = getUserInfo(user_id)
  else:
    user = None
  return render_template('category.html', genre = genre, user = user)


# route: category (books)
@app.route('/catalog/books/')
@app.route('/catalog/book/')
def catalog_books():
  books = session.query(Book).all()
  if 'username' in login_session:
    user_id = getUserID(login_session['email'])
    user = getUserInfo(user_id)
  else:
    user = None
  return render_template('catalog_books.html', books = books, user = user)


# route: books JSON
@app.route('/catalog/book/JSON')
def books_JSON():
  books = session.query(Book).all()
  return jsonify(Books=[b.serialize for b in books])


# route: category (genres)
@app.route('/catalog/genres/')
@app.route('/catalog/genre/')
def catalog_genres():
  genres = session.query(Genre).all()
  return render_template('catalog_genres.html', genres = genres)


# route: genres JSON
@app.route('/catalog/genre/JSON')
def genres_JSON():
  genres = session.query(Genre).all()
  return jsonify(Genres=[g.serialize for g in genres])


# route: category (authors)
@app.route('/catalog/authors/')
@app.route('/catalog/author/')
def catalog_authors():
  authors = session.query(Author).all()
  return render_template('catalog_authors.html', authors = authors)


# route: authors JSON
@app.route('/catalog/author/JSON')
def authors_JSON():
  authors = session.query(Author).all()
  return jsonify(Authors=[a.serialize for a in authors])


# route: item (book)
@app.route('/catalog/book/<int:id>')
def catalog_book(id):
  book = session.query(Book).filter_by(id = id).one()
  if 'username' in login_session:
    user_id = getUserID(login_session['email'])
    user = getUserInfo(user_id)
  else:
    user = None
  return render_template('book.html', book = book, user = user)


# route: book JSON
@app.route('/catalog/book/<int:id>/JSON')
def book_JSON(id):
  book = session.query(Book).filter_by(id=id).one()
  return jsonify(Book=book.serialize)


# route: create item (book)
@app.route('/catalog/book/create', methods=['GET', 'POST'])
def create_book():
  if 'username' not in login_session:
    return redirect(url_for('login'))
  if request.method == "POST":
    new_book = Book(title=request.form['title'], cover=request.form['cover'], description=request.form['description'])
    session.add(new_book)
    try:
      for author_id in request.form.getlist('author'):
        append_author = session.query(Author).filter_by(id=author_id).one()
        new_book.authors.append(append_author)
      for genre_id in request.form.getlist('genre'):
        append_genre = session.query(Genre).filter_by(id=genre_id).one()
        new_book.genres.append(append_genre)
    except:
      e = sys.exc_info()[0]
      print "error: {}".format(e)
    session.commit()
    flash("{} has been created!".format(new_book.title))
    return redirect(url_for('catalog_books'))
  else:
    authors = session.query(Author).all()
    genres = session.query(Genre).all()
    return render_template('book_create.html', authors = authors, genres = genres)


# route: edit item (book)
@app.route('/catalog/book/<int:id>/edit', methods=['GET', 'POST'])
def edit_book(id):
  if 'username' not in login_session:
    return redirect(url_for('login'))
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
    flash("{} has been updated!".format(book.title))
    return redirect(url_for('catalog_book', id = book.id))
  else:
    return render_template('book_edit.html', book = book)


# route: delete item (book)
@app.route('/catalog/book/<int:id>/delete', methods=['GET', 'POST'])
def delete_book(id):
  if 'username' not in login_session:
    return redirect(url_for('login'))
  book = session.query(Book).filter_by(id = id).one()
  if request.method == 'POST':
    session.delete(book)
    session.commit()
    flash("{} has been removed from the catalog".format(book.title))
    return redirect(url_for('catalog_books'))
  else:
    return render_template('book_delete.html', book = book)


# route: item (genre)
@app.route('/catalog/genre/<int:id>')
def catalog_genre(id):
  genre = session.query(Genre).filter_by(id = id).one()
  return render_template('genre.html', genre = genre)


# route: genre JSON
@app.route('/catalog/genre/<int:id>/JSON')
def genre_JSON(id):
  genre = session.query(Genre).filter_by(id=id).one()
  return jsonify(Genre=genre.serialize)


# route: create item (genre)
@app.route('/catalog/genre/create', methods=['GET', 'POST'])
def create_genre():
  if 'username' not in login_session:
    return redirect(url_for('login'))
  if request.method == "POST":
    new_genre = Genre(type=request.form['type'])
    session.add(new_genre)
    try:
      for book_id in request.form.getlist('book'):
        append_book = session.query(Book).filter_by(id=book_id).one()
        new_genre.books.append(append_book)
    except:
      e = sys.exc_info()[0]
      print "error: {}".format(e)
    session.commit()
    return redirect(url_for('catalog_genres'))
  else:
    books = session.query(Book).all()
    return render_template('genre_create.html', books = books)


# route: edit item (genre)
@app.route('/catalog/genre/<int:id>/edit', methods=['GET', 'POST'])
def edit_genre(id):
  if 'username' not in login_session:
    return redirect(url_for('login'))
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
  if 'username' not in login_session:
    return redirect(url_for('login'))
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

# route: author JSON
@app.route('/catalog/author/<int:id>/JSON')
def author_JSON(id):
  author = session.query(Author).filter_by(id=id).one()
  return jsonify(Author=author.serialize)


# route: create item (author)
@app.route('/catalog/author/create', methods=['GET', 'POST'])
def create_author():
  if 'username' not in login_session:
    return redirect(url_for('login'))
  if request.method == "POST":
    new_author = Author(first_name=request.form['first_name'], last_name=request.form['last_name'], bio=request.form['bio'])
    session.add(new_author)
    try:
      for book_id in request.form.getlist('book'):
        append_book = session.query(Book).filter_by(id=book_id).one()
        new_author.books.append(append_book)
    except:
      e = sys.exc_info()[0]
      print "error: {}".format(e)
    session.commit()
    return redirect(url_for('catalog_authors'))
  else:
    books = session.query(Book).all()
    return render_template('author_create.html', books = books)


# route: edit item (author)
@app.route('/catalog/author/<int:id>/edit', methods=['GET', 'POST'])
def edit_author(id):
  if 'username' not in login_session:
    return redirect(url_for('login'))
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
  if 'username' not in login_session:
    return redirect(url_for('login'))
  author = session.query(Author).filter_by(id = id).one()
  if request.method == 'POST':
    session.delete(author)
    session.commit()
    return redirect(url_for('catalog_authors'))
  else:
    return render_template('author_delete.html', author = author)



if __name__ == '__main__':
  app.secret_key = ''.join(os.urandom(15))
  app.debug = True
  app.run(host='0.0.0.0', port=8000, threaded = False)