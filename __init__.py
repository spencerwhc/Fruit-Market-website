#import flask - from the package import class
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app=Flask(__name__)

#create a function that creates a web application
# a web server will run this web application
def create_app():
    app.debug=True
    app.secret_key='YouWillNeverKnows'

    #set the app configuration data 
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///fruitmarket.sqlite'
    db.init_app(app)

    bootstrap= Bootstrap(app)

    #initialize db with flask app
   
    #importing modules here to avoid circular references, register blueprints of routes
    from . import views
    app.register_blueprint(views.bp)
    # from . import admin
    # app.register_blueprint(admin.bp)
   
    return app


@app.errorhandler(404) 
# inbuilt function which takes error as parameter 
def not_found(e): 
  return render_template("404.html")