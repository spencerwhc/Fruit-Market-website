from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .models import Fruit, Category, Order
from datetime import datetime
from .forms import CheckoutForm
from . import db

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    categories = Category.query.order_by(Category.name).all()
    fruits = Fruit.query.order_by(Fruit.name).all()
    return render_template('index.html', categories=categories, fruits=fruits)


@bp.route('/fruits/<int:fruitid>/')
def fruitDetail(fruitid):
    fruits = Fruit.query.filter(Fruit.id == fruitid)
    return render_template('fruit.html', fruits=fruits)


@bp.route('/fruits/')
def search():
    search = request.args.get('search')
    search = '%{}%'.format(search)
    fruits = Fruit.query.filter(Fruit.description.like(search)).all()
    return render_template('fruit.html', fruits=fruits)


@bp.route('/order', methods=['POST', 'GET'])
def order():

    fruit_id = request.values.get('fruit_id')

    # retrieve order if there is one
    if 'order_id'in session.keys():
        order = Order.query.get(session['order_id'])
        # order will be None if order_id stale
    else:
        # there is no order
        order = None

    # create new order if needed
    if order is None:
        order = Order(status=False, firstname='', lastname='',
                      email='', phone_number='', address='', total_cost=0)
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except:
            print('failed at creating a new order')
            order = None

    # calcultate totalprice
    totalprice = 0
    if order is not None:
        for fruit in order.fruits:
            totalprice = totalprice + fruit.price

    # are we adding an item?
    if fruit_id is not None and order is not None:
        fruit = Fruit.query.get(fruit_id)
        if fruit not in order.fruits:
            try:
                order.fruits.append(fruit)
                db.session.commit()
            except:
                return 'There was an issue adding the item to your basket'
            return redirect(url_for('main.order'))
        else:
            flash('Item already in basket')
            return redirect(url_for('main.order'))

    return render_template('order.html', order=order, totalprice=totalprice)


@bp.route('/deletebasketitem/', methods=['POST'])
def deletebasketitem():
    id = request.form['id']
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        fruit_to_delete = Fruit.query.get(id)
        try:
            order.fruits.remove(fruit_to_delete)
            db.session.commit()
            return redirect(url_for('main.order'))
        except:
            return 'Problem deleting item from order'
    return redirect(url_for('main.order'))


@bp.route('/deletebasket/')
def deletebasket():
    if 'order_id' in session:
        del session['order_id']
        flash('All items deleted')
    return redirect(url_for('main.index'))


@bp.route('/checkout', methods=['POST', 'GET'])
def checkout():
    form = CheckoutForm()
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])

        totalprice = 0
        for fruit in order.fruits:
                totalprice = totalprice + fruit.price

        if form.validate_on_submit():
            order.status = True
            order.firstname = form.firstname.data
            order.lastname = form.lastname.data
            order.email = form.email.data
            order.phone_number = form.phone.data
            order.address = form.address.data
            order.total_cost = totalprice
            order.date = datetime.now()
            try:
                db.session.commit()
                del session['order_id']
                flash('Thank you! Your order has been successfully submitted.')
                return redirect(url_for('main.index'))
            except:
                return 'There was an issue completing your order'
    return render_template('checkout.html', form=form, totalprice=totalprice)
