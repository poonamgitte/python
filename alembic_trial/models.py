from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    age = Column(Integer)
    phone = Column(String)
    address = Column(String)
    
    
    
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


# -------------------------
# Category Model
# -------------------------
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)

    # Relationship (One Category -> Many Products)
    products = relationship("Product", back_populates="category", cascade="all, delete")


# -------------------------
# Product Model
# -------------------------
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)

    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    # Relationship
    category = relationship("Category", back_populates="products")