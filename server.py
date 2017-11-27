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

# POST/DELETE FUNCTIONS

def dynamic_routing():
    """ TODO """
    return -1

def get_articles():
    """ TODO """
    return -1

def search_article():
    """ TODO """
    return -1

def create_article():
    """ TODO """
    return -1

def delete_article():
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
