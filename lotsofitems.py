from database_setup import Base,Item,Shop
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

# Create session and connect to DB
engine = create_engine('postgresql://catalog:password@localhost/catalog')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Shops for db

shop1 = Shop(name="Finish Line")
session.add(shop1)
session.commit()

shop2 = Shop(name="Walmart")
session.add(shop2)
session.commit()

shop3 = Shop(name="American Eagle")
session.add(shop3)
session.commit()

shop4 = Shop(name="Amazon")
session.add(shop4)
session.commit()

shop5 = Shop(name="Forever 21")
session.add(shop5)
session.commit()


# items for store1 FINISH LINE

item1 = Item(title="Nike Shoes",price=69.9,discount_price=65.9,shop=shop1,pic="https://c.static-nike.com/a/images/t_PDP_864_v1/f_auto/cvwpari$

session.add(item1)
session.commit()

item2 = Item(title="Nike Shirt",price=59.9,discount_price=55.9,shop=shop1,pic="https://c.static-nike.com/a/images/t_PDP_864_v1/f_auto/xbwy3vz$

session.add(item2)
session.commit()

item3 = Item(title="Nike Coat",price=59.9,discount_price=55.9,shop=shop1,pic="https://c.static-nike.com/a/images/t_PDP_864_v1/f_auto/qgir57n6$

session.add(item3)
session.commit()

item4 = Item(title="Nike Shirt",price=49.9,discount_price=25.9,shop=shop1,pic="https://c.static-nike.com/a/images/t_PDP_1728_v1/f_auto/lztfne$

session.add(item4)
session.commit()

item5 = Item(title="Nike Sandal",price=29.9,discount_price=25.9,shop=shop1,pic="https://c.static-nike.com/a/images/t_PDP_1728_v1/f_auto/sxkkn$

session.add(item5)
session.commit()

session.add(item6)
session.commit()

# items for store2 WALMART

item2_1 = Item(title="Cookware",price=94.9,discount_price=74.9,shop=shop2,pic="https://www.coghlans.com/images/products/products-camp-kitchen$

session.add(item2_1)
session.commit()

item2_2 = Item(title="Headphones",price=149.9,discount_price=125.9,shop=shop2,pic="http://demo.ajax-cart.com/photos/product/4/176/4.jpg",bran$

session.add(item2_2)
session.commit()

item2_3 = Item(title="Finger Nail Polish",price=19.9,discount_price=15.9,shop=shop2,pic="https://www.photigy.com/wp-content/uploads/2013/09/p$

session.add(item2_3)
session.commit()

item2_4 = Item(title="Greek Yogurt",price=3.9,discount_price=2.9,shop=shop2,pic="http://i.dailymail.co.uk/i/pix/2013/05/22/article-2329246-19$

session.add(item2_4)
session.commit()

item2_5 = Item(title="Shampoo and Conditioner",price=9.9,discount_price=5.9,shop=shop2,pic="http://121clicks.com/wp-content/uploads/2011/09/p$

session.add(item2_5)
session.commit()

item2_6 = Item(title="iPad",price=129.9,discount_price=119.9,shop=shop2,pic="http://www.deepetch.com/blog/wp-content/uploads/2015/04/product-$

session.add(item2_6)
session.commit()


# items for store3 AMERICAN EAGLE

item3_1 = Item(title="T-Shirt",price=29.9,discount_price=25.9,shop=shop3,pic="https://uploads-ssl.webflow.com/56c3dacdc7a3965c44668616/587905$

session.add(item3_1)
session.commit()

item3_2 = Item(title="Polo Shirt",price=49.9,discount_price=25.9,shop=shop3,pic="https://www.publicdomainpictures.net/pictures/190000/velka/t$

session.add(item3_2)
session.commit()

item3_3 = Item(title="Dress Shirt",price=49.9,discount_price=25.9,shop=shop3,pic="https://cdn.pixabay.com/photo/2016/02/07/14/59/shirts-11849$

session.add(item3_3)
session.commit()

item3_4 = Item(title="Jeans",price=49.9,discount_price=25.9,shop=shop3,pic="https://assets.academy.com/mgen/04/10606904.jpg",brand="AMERICAN $

session.add(item3_4)
session.commit()

item3_5 = Item(title="Shorts",price=29.9,discount_price=25.9,shop=shop3,pic="https://kathmandu.imgix.net/catalog/product/1/2/12343_sendattrav$

session.add(item3_5)
session.commit()

item3_6 = Item(title="Belt",price=29.9,discount_price=25.9,shop=shop3,pic="https://images-na.ssl-images-amazon.com/images/I/81wqPZ9znDL._UX67$

session.add(item3_6)
session.commit()

# items for store4 AMAZON

item4_1 = Item(title="Laptop",price=419.9,discount_price=415.9,shop=shop4,pic="https://images-na.ssl-images-amazon.com/images/I/31BbTpqDXxL._$

session.add(item4_1)
session.commit()

item4_2 = Item(title="Camera Drone",price=149.9,discount_price=125.9,shop=shop4,pic="https://images-na.ssl-images-amazon.com/images/I/41f6jAE$

session.add(item4_2)
session.commit()

item4_3 = Item(title="Boots",price=49.9,discount_price=25.9,shop=shop4,pic="https://images-na.ssl-images-amazon.com/images/I/410oz0sMTkL.__AC$

session.add(item4_3)
session.commit()

item4_4 = Item(title="Easter Egg Kit",price=12.9,discount_price=10.9,shop=shop4,pic="https://images-na.ssl-images-amazon.com/images/I/51s3QDV$

session.add(item4_4)
session.commit()

item4_5 = Item(title="Gas Cap",price=9.9,discount_price=5.9,shop=shop4,pic="https://images-na.ssl-images-amazon.com/images/I/51hKM0xqm5L._AC_$

session.add(item4_5)
session.commit()

item4_6 = Item(title="Bobble Head",price=19.9,discount_price=15.9,shop=shop4,pic="https://images-na.ssl-images-amazon.com/images/I/51t700JTNG$

session.add(item4_6)
session.commit()


# items for store5 FOREVER 21

item5_1 = Item(title="Windbreaker Jacket",price=29.9,discount_price=25.9,shop=shop5,pic="https://www.forever21.com/images/default_330/0025693$

session.add(item5_1)
session.commit()

item5_2 = Item(title="Yoga Pants",price=39.9,discount_price=25.9,shop=shop5,pic="https://www.forever21.com/images/default_330/00257847-01.jpg$

session.add(item5_2)
session.commit()

item5_3 = Item(title="Striped Pants",price=49.9,discount_price=35.9,shop=shop5,pic="https://www.forever21.com/images/default_330/00255074-02.$

session.add(item5_3)
session.commit()

item5_4 = Item(title="Swimsuit",price=69.9,discount_price=65.9,shop=shop5,pic="https://www.forever21.com/images/default_330/00269948-02.jpg",$

session.add(item5_4)
session.commit()

item5_5 = Item(title="Sunglasses",price=19.9,discount_price=15.9,shop=shop5,pic="https://www.forever21.com/images/default_330/00245829-01.jpg$

session.add(item5_5)
session.commit()

item5_6 = Item(title="Jean Jacket",price=39.9,discount_price=35.9,shop=shop5,pic="https://www.forever21.com/images/default_330/00269955-01.jp$

session.add(item5_6)
session.commit()
