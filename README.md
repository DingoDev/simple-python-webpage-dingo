# simple-python-webpage-dingo

G'day there, see you've got a copy of my website article template.
Now before you go let your kangaroos out in the paddock reading the
source code, I've written down what you need to know before you go
chuke a bluey in the issues field.

This is a work in progress and until all the nice backend features are
completed you will need to solve out many of these manually, away from
a web interface.

First off you're going to need to set up your admin profile in the
database. Just alter the file in the appropriate place to change the
password. It would be preferable if you put the sha256 hexadecimal hash
as the password instead of clear text.

To get this hash, follow these commands

python3
> import hashlib

> sha256 = hashlib.sha256('your_password').hexdigest()

Take the output and copy it into the database

To run the app, go into the terminal and type
python3 ./server.py

PICTURES
If you want to store your own images on the server instead of some
content storage. Then place all images inside the static folder and
copy the url_for used for styling and javascript.