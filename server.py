""" Base server to run on Flask """
import hashlib
import sys
import os

# GLOBAL VARIABLES
PIP_IMPORTED = False
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

try:
    from flask import Flask, abort, flash, redirect, render_template, request, url_for
except ImportError:
    import pip
    PIP_IMPORTED = True
    pip.main(['install', '--user', 'flask'])
    from flask import Flask, abort, flash, redirect, render_template, request, url_for

try:
    from flask.ext.sqlalchemy import SQLAlchemy
except ImportError:
    if not PIP_IMPORTED:
        import pip
        PIP_IMPORTED = True
    pip.main(['install', '--user', 'flask-sqlalchemy'])
    from flask.ext.sqlalchemy import SQLAlchemy


# SETUP APPLICATION AND DATABASE
APPLICATION = Flask(__name__)
APPLICATION.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'data.db')
APPLICATION.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

DATABASE = SQLAlchemy(APPLICATION)

CONFIG = {'port': 5000}

# DATABASE RELATIONSHIPS

class Article_list(DATABASE.model):
    """ 
        I originally didn't think it would be necessary to split articles 
        Then I was like, right articles have categories
        Easier to set up the DB this way anyways
    """
    __tablename__ = 'article_lists'
    id = DATABASE.Column(DATABASE.Integer, primary_key=True)
    list_type = DATABASE.Column(DATABASE.String(), unique=True)
    articles = DATABASE.relationship('Article', backref='article_list')
    
class Article(DATABASE.model):
    """
        So this is supposed to be super simple
        The content id is how you will find the article via the /article/{id}
        The content stores your actual article, use it to store the html parts
        such as <h2>trashy waifus</h2> <img src="your_waifu.jpg"/>
    """
    __tablename__ = 'articles'
    id = DATABASE.Column(DATABASE.Integer, primary_key=True)
    content_id = DATABASE.Column(DATABASE.Integer, unique=True, index=True)
    content = DATABASE.Column(DATABASE.String(5000)) # Change the 5000 to whatever you think is your general article length + styling additions/images

class Role(DATABASE.model):
    """
        If you can be bothered with having multiple types of users
    """
    __tablename__ = 'roles'
    id = DATABASE.Column(DATABASE.Integer, primary_key=True)
    users = DATABASE.relationship('User', backref='Role')

class User(DATABASE.model):
    """
        We're going to start off real simple with one user for you, the creator
        You know the deal though, username and password
    """
    __tablename__ = 'users'
    id = DATABASE.Column(DATABASE.Integer, primary_key=True)
    username = DATABASE.Column(DATABASE.Integer, unique=True, index=True)
    password = DATABASE.Column(DATABASE.Integer)

# GET ROUTING

@APPLICATION.route('/')
def show_home():
    """ Show the home page """
    return render_template("home.html")

@APPLICATION.route('/contact')
def show_contact():
    """ Show the contact page """
    return render_template("contact.html")

@APPLICATION.route('/article/<id>')
def serve_article():
    """ TODO """
    # Get article content based on the id
    articles = {'123964': '<h2>This is a new article</h2>'}
    content = articles['123964']
    return render_template("article.html", content=content)

@APPLICATION.route('/article')
def get_articles():
    """ TODO """
    req_header = request.headers
    no_of_articles = req_header['no_of_articles']
    index = req_header['index']
    article_list_type = req_header['article_list']
    return -1

def search_article():
    """ TODO """
    req_header = request.headers
    keywords = req_header['keywords']
    return -1

# POST/DELETE FUNCTIONS

def dynamic_routing():
    """ TODO """
    return -1

@APPLICATION.route('/api/article/create', methods=['POST'])
# login required
def create_article():
    """ TODO """
    return -1

@APPLICATION.route('/api/article/delete', methods=['DELETE'])
def delete_article():
    """ TODO """
    return -1

@APPLICATION.route('/api/user/create', methods=['POST'])
def create_user():
    """ TODO """
    return -1

@APPLICATION.route('/api/user/delete', methods=['POST'])
def delete_user():
    """ TODO """
    return -1

@APPLICATION.route('/api/user/password', methods=['PUT'])
def change_password():
    """ TODO """
    return -1

@APPLICATION.route('/api/user/role', methods=['PUT'])
def change_role():
    """ TODO """
    return -1

@APPLICATION.route('/api/role/create', methods=['POST'])
def create_role():
    """ TODO """
    return -1

@APPLICATION.route('/api/role/delete', methods=['DELETE'])
def delete_role():
    """ TODO """
    return -1

# MY BASIC ATTEMPT AT MAKING AUTHENTICATION WILL CHANGE

def authenticate(request_rec):
    """ TODO """
    # Replace with users list
    users = {'user': 'hexdigest'}

    # user = users[request.headers['username']]
    user = users['user']
    if not user:
        return False

    sha256 = hashlib.sha256(request_rec.headers['password']).hexdigest()

    # Is it the correct user password
    authenticated = (user == sha256)

    # Erase previous passwords hash from the stack
    sha256 = hashlib.md5("asdfghjklkmnbvcxzaqwertyuiop0987654321")

    return authenticated

# MAIN LIFECYCLE

def read_config():
    """ Read the server.config file and update the CONFIG dictionary """
    try:
        with open("server.config") as config:
            for conf in config.readlines():
                values = conf.split('=')
                CONFIG[values[0]] = values[1]
    except Exception:
        return -1
    return 0

if __name__ == "__main__":
    if read_config() == -1:
        sys.exit(-1)
    dynamic_routing()
    APPLICATION.run(host='0.0.0.0', port=CONFIG['port'])
