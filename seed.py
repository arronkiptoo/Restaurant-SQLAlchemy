from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Restaurant, Customer, Review

# Create a SQLite database and bind it to SQLAlchemy models
engine = create_engine('sqlite:///restaurant_reviews.db')
Base.metadata.create_all(engine, checkfirst=True)  # Create the database schema

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create sample data
restaurant1 = Restaurant(name='Kibandaski', price=3)
restaurant2 = Restaurant(name='prestige', price=2)
customer1 = Customer(first_name='Mark', last_name='Peter')
customer2 = Customer(first_name='Aaron', last_name='Kiptoo')

review1 = Review(star_rating=4, restaurant=restaurant1, customer=customer1)
review2 = Review(star_rating=5, restaurant=restaurant2, customer=customer2)


# Add data to the session and commit
session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2])
session.commit()