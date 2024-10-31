from flask import Flask
import secrets


app = Flask("HAGZ")
app.config['SECRET_KEY'] = secrets.token_hex(16)

from app import routes
