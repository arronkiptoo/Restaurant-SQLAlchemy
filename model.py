from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Restaurant(Base):
    # Define the 'restaurants' table
    __tablename__ = 'restaurants'

    # Define columns for the 'restaurants' table
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    # Establish relationships with other tables
    reviews = relationship('Review', back_populates='restaurant')  # One-to-many relationship with 'reviews'
    customers = relationship('Customer', secondary='reviews', back_populates='restaurants')  # Many-to-many relationship with 'customers'

class Customer(Base):
    # Define the 'customers' table
    __tablename__ = 'customers'

    # Define columns for the 'customers' table
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    # Establish relationships with other tables
    reviews = relationship('Review', back_populates='customer')  # One-to-many relationship with 'reviews'
    restaurants = relationship('Restaurant', secondary='reviews', back_populates='customers')  # Many-to-many relationship with 'restaurants'
   
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Review(Base):
    # Define the 'reviews' table
    __tablename__ = 'reviews'

     # Define columns for the 'reviews' table
    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    # Establish relationships with other tables
    restaurant = relationship('Restaurant', back_populates='reviews')  # Many-to-one relationship with 'restaurants'
    customer = relationship('Customer', back_populates='reviews')  # Many-to-one relationship with 'customers'