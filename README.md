#Udacity Catalog Project

This is a library CRUD web app for the udacity full-stack web developer catalog project. The app incorporates Flask, SQLAlchemy, JS, and HTML, allowing you to view a collection of books, authors, and genre categories—or register and add your own! Feel free to check it out and build your own book library/wishlist!

##Requirements

* You'll need [Python](https://www.python.org/) and a working computer to view or edit this project.
* A virtual machine to run everything. This app relies on [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/).

##Installation

1. Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/) on your computer.
2. Download the [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm).
  - [`Clone`](https://github.com/udacity/fullstack-nanodegree-vm.git) the Udacity-created Vagrant file.
3. [`Clone`](https://github.com/purwin/Udacity_Log_Analysis.git) this project within the Vagrant directory so you have the working files on your computer.
4. Start up your Vagrant file. Run the following in Terminal in your Vagrant directory:
    * `vagrant up`
    * `vagrant ssh`
    * `cd /vagrant` to access project files
5. `cd` to the cloned `Udacity_Catalog` directory, and run `python views.py`.
6. Open your web browser of choice and type in the following address to view the app: `http://localhost:8000`
7. Check out those beautiful RESTful app routes!

##API

This web app features RESTful routes, so feel free to peruse the app and pull data from the various JSON endpoints:
* `/catalog/books/JSON`: View data for all books in the database
* `/catalog/genres/JSON`: View data for all genre categories in the database
* `/catalog/authors/JSON`: View data for all authors in the database
* `/catalog/book/#/JSON`: View data for an individual book in the database
* `/catalog/genre/#/JSON`: View data for an individual genre category in the database
* `/catalog/author/#/JSON`: View data for an individual author in the database

##FAQ

* Q: I can't edit book or author or genre data. How do I do that?
* A: You need to be logged in to edit material, and you need to be the creator of said book/author/data to edit any information. Create your own

* Q: How do I create a book/author/genre?
* A: If you're logged in, simply go to the relevant create routes and type away!

* Q: Can I login without a Google or GitHub account?
* A: Not at present. Stay tuned for updates!

##Contribute!

Feel free to `clone` or `fork` this project!