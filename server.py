""" Base server to run on Flask """
import hashlib
from flask import Flask, abort, flash, redirect, render_template, request, url_for
import sys

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

def serve_article():
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

def authenticate(request_rec):
    """ TODO """
    # Replace with users list
    users = {'user': 'hexdigest'}

    # user = users[request.headers['username']]
    user = users['user']

    sha256 = hashlib.sha256(request_rec.headers['password']).hexdigest()

    # Is it the correct user password
    authenticated = (user == sha256)

    # Erase previous passwords hash from the stack
    sha256 = hashlib.md5("asdfghjklkmnbvcxzaqwertyuiop0987654321")

    return authenticated

def read_config():
    """ TODO """
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
