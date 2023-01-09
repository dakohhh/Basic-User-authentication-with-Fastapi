from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text , ForeignKey, DECIMAL, SmallInteger
from sqlalchemy.orm import relationship
from .database import Base
from controller.hex import generate_hex

from datetime import datetime




class User(Base):
    __tablename__ = "users"

    user_id = Column(String(12), primary_key=True, nullable=False, index=True)

    fullname = Column(String(20), nullable=False, unique=True)

    email = Column(String(200), nullable=False, unique=True)

    password = Column(String(200), nullable=False)

    is_verified = Column(Boolean, default=False)

    role = Column(SmallInteger, nullable=False, default=1)

    token_verification = Column(String(40), nullable=True)

    id_expire = Column(TIMESTAMP)

    date_added = Column(TIMESTAMP, server_default=text("NOW()"))

    # cart_add = relationship("Cart", back_populates="user")




class Products(Base):
    __tablename__ = "products"
    
    product_id = Column(String(100), primary_key=True, index=True)
    
    product_name = Column(String(100), nullable=False, index=True)
    
    category = Column(String(30), index=True)
    
    original_price = Column(DECIMAL(7, 2), nullable=False)

    new_price = Column(DECIMAL(7, 2), nullable=True)

    discount = Column(Integer, nullable=True)
    
    date_added =  Column(TIMESTAMP, server_default=text("NOW()"))
    

class Cart(Base):
    __tablename__ = "carts"

    cart_id = Column(Integer, primary_key=True, autoincrement=True, index=True)

    product_id =  Column(String(100),  ForeignKey("products.product_id"), nullable=False)

    user_id = Column(String(100),  ForeignKey("users.user_id"), nullable=False)

    date_added = Column(TIMESTAMP, server_default=text("NOW()"))

    # user = relationship("User", back_populates="cart_added")