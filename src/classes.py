from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, Float

Base = declarative_base()


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    comment = Column(String(200), nullable=False)

    def __init__(self, name, price, quantity, comment):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.comment = comment

    def __repr__(self):
        return "<Product('%s','%s', '%s', '%s', '%s')>" % \
               (self.id, self.name, self.price, self.quantity, self.comment)
