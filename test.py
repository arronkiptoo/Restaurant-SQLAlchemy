from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Restaurant, Customer, Review

# Create a SQLite database and bind it to SQLAlchemy models
engine = create_engine('sqlite:///restaurant_reviews.db')

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Test methods
restaurant = session.query(Restaurant).filter_by(name='Restaurant A').first()
reviews_for_restaurant = restaurant.reviews

for review in reviews_for_restaurant:
    # Access the customer and review attributes
    customer = review.customer
    print(f"Review for {restaurant.name} by {customer.full_name()}: {review.star_rating} stars")

# Close the session
session.close()
