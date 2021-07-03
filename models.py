from . import db


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    fruits = db.relationship('Fruit', backref='Category',
                             cascade="all, delete-orphan")

    def __repr__(self):
        str = "Id: {}, Name: {}, Descriptiop: {}"
        str = str.format(self.id, self.name, self.description)
        return str


orderdetails = db.Table('orderdetails',
                        db.Column('order_id', db.Integer, db.ForeignKey(
                            'orders.id'), nullable=False),
                        db.Column('fruit_id', db.Integer, db.ForeignKey(
                            'fruits.id'), nullable=False),
                        db.PrimaryKeyConstraint('order_id', 'fruit_id'))


class Fruit(db.Model):
    __tablename__ = "fruits"
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    name = db.Column(db.String(64), unique=True, nullable=False)
    price= db.Column(db.Float, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(60), nullable=False)
    seasonality = db.Column(db.String(60), nullable=False)
    taste = db.Column(db.String(500), nullable=False)
    made_from = db.Column(db.String(60), default='grown-in-au-logo.svg')
    

    def __repr__(self):
        str = "Id: {}, Category: {}, Name: {}, Price: ${},Description: {}, Image: {}, Seasonality:{},Taste:{}, Made From:{}\n"
        str = str.format(self.id, self.category_id, self.name, self.price, self.description, self.image,
                         self.seasonality, self.taste, self.made_from)
        return str


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    fruits = db.relationship("Fruit", secondary=orderdetails, backref="orders")
    total_cost = db.Column(db.Float)
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    email = db.Column(db.String(128))
    phone_number = db.Column(db.String(32))
    address = db.Column(db.String(200))
    date = db.Column(db.DateTime)

    def __repr__(self):
        str = "Id: {}, Status: {}, Fruits:{}, Total Cost:{}, Firstname: {}, Lastname: {}, Email: {}, Phone Number: {}, Address:{}, Date: {}\n"
        str = str.format(self.id, self.status, self.fruits,
                         self.total_cost, self.firstname, self.lastname, self.email, self.phone_number, self.address, self.date)
        return str
