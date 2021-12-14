from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123456789 987654321' #this key is important and should be private in production
    return app
#this created the flask application
