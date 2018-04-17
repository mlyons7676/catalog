from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import  create_engine

Base = declarative_base()

class Item(Base):
    __tablename__ = 'item'
    title = Column(String(100), nullable = False, index = True)
    price = Column(Integer, nullable = True)
    discount_price=Column(Integer, nullable = True)
    id = Column(Integer, primary_key = True)
    brand= Column(String(20), nullable = True, index = True)
    pic = Column(String(200),nullable = True)
    shop_id = Column(Integer, ForeignKey("shop.id"),nullable=True)
    shop=relationship("Shop")

    @property
    def serialize_item(self):
        return {
            'title': self.title,
            'price': self.price,
            'discount_price': self.discount_price,
            'brand' : self.brand,
            'shop': self.shop.id
        }

class Shop(Base):
    __tablename__ = 'shop'
    id = Column(Integer,primary_key=True)
    name = Column(String(20), nullable = False, index = True)
    Item = relationship("Item")

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'Item': [i.serialize_item for i in self.Item]
        }


engine = create_engine('sqlite:///item.db')

Base.metadata.create_all(engine)