from flask import Blueprint
from . import db
from .models import Category, Fruit, Order


bp = Blueprint('admin', __name__, url_prefix='/admin/')

# function to put some seed data in the database
@bp.route('/dbseed/')
def dbseed():
    cat1 = Category(name='apple', description='Apples are rich in fiber, vitamins, and minerals, all of which benefit health. They also provide an array of antioxidants. These substances help neutralize free radicals.')
    cat2 = Category(name='banana', description='Banana is very low in Saturated Fat, Cholesterol and Sodium. It is also a good source of Dietary Fiber, Vitamin C, Potassium and Manganese, and a very good source of Vitamin B6.')
    cat3 = Category(
        name='orange', description='Oranges are a healthy source of fiber, vitamin C, thiamine, folate, and antioxidants.')
    try:
        db.session.add(cat1)
        db.session.add(cat2)
        db.session.add(cat3)
        db.session.commit()
    except:
        return 'There was an issue adding the category in dbseed function'

    fruit1 = Fruit(category_id=cat1.id, name='Envy Apple(each)', price=1.20, description='Envy apples are a round variety with striated, ruby red skin with green undertones.',
                   image='Envy Apple .jpg', seasonality='All Year Round', taste='Sweet with low acid and a slightly flowery taste.', made_from='')
    fruit2 = Fruit(category_id=cat1.id, name='Pink Lady Apple(each)', price=1.70, description='Pink Lady Apple\'s tender skin has a pink to reddish-pink blush over a yellow background.',
                   image='Fresh Pink Lady Apples .jpg', seasonality='Late Autumn into Spring', taste='Sweet-tart flavour with crunchy texture and effervescent finish.', made_from='')
    fruit3 = Fruit(category_id=cat1.id, name='Royal Gala Apple(each)', price=1.55, description='Royal Gala apples are covered in a thin yellow to gold skin, highlighted with pink to red stripes that vary in hue dependent upon the apples maturity.',
                   image='Apple Royal Gala .jpg', seasonality='All Year Round', taste='Their dense flesh is creamy yellow and crisp, offering a mildly sweet flavor and flora aroma.develop.', made_from='')
    fruit4 = Fruit(category_id=cat2.id, name='Banana Lady Finger (5pc)', price=7.45, description='Lady Finger bananas have thin, bright yellow skins that will develop dark flecks when fully ripe.',
                   image='Banana Lady Finger each.jpg', seasonality='All Year Round', taste='The fruit has a creamy consistency, with a sweeter flavor than common bananas.', made_from='')
    fruit5 = Fruit(category_id=cat2.id, name='Dwarf Cavendish Banana (5pc)', price=5.20, description='Dwarf cavendish bananas are the most common variety. They are the long yellow, slightly sweet bananas at supermarkets around the U.S.',
                   image='Cavendish Banana.jpg', seasonality='All Year Round', taste='Mild and Sweet.', made_from='')
    fruit6 = Fruit(category_id=cat2.id, name='Little Sana Banana (5pc)', price=3.45, description='Little Sana Bananas are purposely chosen for their size and eating characteristics. They are grown at the lower end of the bunch, making them smaller in size than regular bananas they still contain all the natural nutritional qualities of its big brother, the regular Cavendish bananas.',
                   image='Little Sana Banana.jpg', seasonality='All Year Round', taste='Creamy, smooth texture and mild sweetness.', made_from='')
    fruit7 = Fruit(category_id=cat3.id, name='Organic Navel Orange(net)', price=7.99, description='Organic Navel Orange is a more healthy option for you! Its nutrients in about half of a large orange.',
                   image='Organic Navel Oranges .jpg', seasonality='Winter - Spring', taste='They are seedless, with a superior rich flavor nicely balanced between sugar and acid. ', made_from='')
    fruit8 = Fruit(category_id=cat3.id, name='Orange Navel(each)', price=1.20, description='Navel oranges are medium to large in size, averaging 6-10 centimeters in diameter, and are globular to slightly oval in shape with the trademark “navel” or circular hole on the blossom stem end.',
                   image='Orange Navel .jpg', seasonality='Winter - Spring', taste='Navel oranges are aromatic, sweet, and contain a low-acidity which produces a balanced level of sweet, tangy, and tart flavors.', made_from='')

    try:
        db.session.add(fruit1)
        db.session.add(fruit2)
        db.session.add(fruit3)
        db.session.add(fruit4)
        db.session.add(fruit5)
        db.session.add(fruit6)
        db.session.add(fruit7)
        db.session.add(fruit8)
        db.session.commit()
    except:
        return 'There was an issue adding a fruit in dbseed function'

    return 'DATA LOADED'
