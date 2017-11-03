from flask import Flask, render_template, request, redirect
from flask import jsonify, url_for, flash, make_response
from flask import session as login_session
from sqlalchemy import create_engine, asc, desc, func
from sqlalchemy.orm import sessionmaker
from dbsetup import Base, Category, Item, User


app = Flask(__name__)

# Connect to Database and create database session

engine = create_engine('postgresql://pythonflask:pythonflask@localhost:5432/itemcat')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
# Cats for list of catalogs
cats = session.query(Category).order_by(Category.id)

# Homepage

@app.route("/")
def home():
    items = session.query(Item, Category).join(Category)\
            .order_by(desc(Item.id)).limit(10).all()
    return render_template("index.html", cats=cats, items=items)
##    return "Hi there. I am still alive"

# Show items in a category

@app.route('/catitems/<cat_name>/<int:cat_id>/items/')
def cat(cat_name, cat_id):
    items = session.query(Item).filter_by(category_id=cat_id).all()
    cat = session.query(Category).filter_by(id=cat_id).one()
    return render_template('items.html', cats=cats, items=items,
                           cat=cat)

# Show an item

@app.route('/catitems/<int:cat_id>/<item_name>/<int:item_id>')
def item(cat_id, item_name, item_id):
    item = session.query(Item).filter_by(id=item_id).one()
    cat = session.query(Category).filter_by(id=cat_id).one()
    return render_template('item.html', cats=cats, item=item,
                           cat=cat)


@app.route("/test/")
def test():
    return render_template("test.html")


if __name__ == "__main__":
    app.run()
