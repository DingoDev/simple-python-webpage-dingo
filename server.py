""" Base server to run on Flask """
import hashlib
import sys

try:
    from flask import Flask, abort, flash, redirect, render_template, request, url_for
except Exception:
    import pip
    pip.main(['install', '--user', 'flask'])
    from flask import Flask, abort, flash, redirect, render_template, request, url_for


APPLICATION = Flask(__name__)

CONFIG = {'port': 5000}

@APPLICATION.route('/')
def show_home():
    """ Show the home page """
    return render_template("home.html")

@APPLICATION.route('/contact')
def show_contact():
    """ Show the contact page """
    return render_template("contact.html")

def dynamic_routing():
    """ TODO """
    return -1

def get_articles():
    """ TODO """
    return -1

@APPLICATION.route('/article/<id>')
def serve_article():
    """ TODO """
    # Get article content
    articles = {'123964': '<h2>This is a new article</h2>'}
    content = articles['123964']
    return render_template("article.html", content=content)

def search_article():
    """ TODO """
    return -1

def create_article():
    """ TODO """
    return -1

def delete_article():
    """ TODO """
    return -1

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
