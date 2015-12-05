import psycopg2

import sys

from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine) 
session = Session()
Base = declarative_base()


from datetime import datetime 

from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, desc
from sqlalchemy.orm import relationship



class User(Base):
    __tablename__ = "users" 
     
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable = False)
    password = Column(String, nullable = False)
    
    """One to many relationship with Item for auctioning"""
    items_auctioned = relationship("Items Auctioned", backref="Seller")
    
    """One to many relationship with Bids made"""
    bids = relationship("Bids", backref = "Bidder")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)

    """One to many relationship with User for auctioning"""
    seller_id = Column(ForeignKey("User.id"), nullable = False)
    
    """ One to many relationship with Bids for bids placed on it"""
    Bids = relationship("Bids", backref="Item")



class Bid(Base):
    __tablename__ = "bids"
    
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    
    """ One to many relationship with Items """
    Item_id = Column(ForeignKey("Item.id"), nullable = False)

    """ One to many relationship with Users """
    User_id = Column(ForeignKey("User.id"), nullable = False)
    
Base.metadata.create_all(engine)

results = session.query(Bid.price).order_by(desc(Bid.price)).first()
print(results)