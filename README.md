# Restaurant Reviews Application

## Author
### Aaron Kiptoo

## Description:
This is a simple restaurant reviews application built using Python and SQLAlchemy. Users can add restaurants, leave reviews, and view restaurant details. This project serves as a basic example of creating a web application with a relational database backend.


## Table of Contents
- [Features](#features)
- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Class Descriptions](#class-descriptions)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Features

- Add new restaurants with their name and price range.
- Leave reviews for restaurants with a star rating and comments.
- View restaurant details including average rating and reviews.
- Simple web interface for interacting with the application.

## Introduction
In this project, we have developed a simple yet powerful restaurant review system. The core components of our system include:
- `Customer`: This class represents the individuals who can provide valuable reviews based on their dining experiences. Customers have unique attributes and can interact with the system in various ways.
- `Restaurant`: The Restaurant class is designed to capture information about different dining establishments. It includes details such as the restaurant's name, pricing range, and the ability to receive reviews from customers.
- `Review`: Reviews are at the heart of our system. They are written by customers to share their opinions and star ratings for specific restaurants. Each review is associated with a customer and a restaurant, creating a network of feedback

## Technologies Used

    * Python: Python is a popular high-level programming language known for its simplicity, readability, and versatility.

    * SQLAlchemy: SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
    It provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language.

## Installation
To get started with project, follow these steps:

Clone the repository to your local machine using the following command:

    * git@github.com:arronkiptoo/Restaurant-SQLAlchemy.git

Navigate to the project directory:
    
    * cd Restaurant-SQLAlchemy

Install the required dependencies:

    * pipenv --python 3.10
    
    * pipenv install

    * pipenv shell

    * pip install SQLAlchemy

    * Sudo apt install alembic

## Usage

    The project demonstrates how to establish relationships between classes, create instances, and use the provided methods for interacting with those instances.


# Class Descriptions

## Customer

        Description: A Customer represents an individual who interacts with the application. Customers are users of the application who can leave reviews for restaurants and add new restaurants to the database.
    Attributes:
        id (Integer): A unique identifier for each customer.
        name (String): The name of the customer.
    Relationships:
        reviews (One-to-Many): A customer can leave multiple reviews for different restaurants.
        restaurants (Many-to-Many): Customers can add restaurants to their favorites or keep a list of restaurants they've visited.

## Restaurant

    Description: A Restaurant represents a dining establishment that users can review or add to the application's database. Restaurants have details such as their name and price range.
    Attributes:
        id (Integer): A unique identifier for each restaurant.
        name (String): The name of the restaurant.
        price (Integer): Represents the price range of the restaurant (e.g., 1 for low cost, 5 for high-end).
    Relationships:
        reviews (One-to-Many): Multiple reviews can be associated with a restaurant.
        customers (Many-to-Many): The application tracks which customers have added this restaurant to their favorites or visited list.

## Review

        Description: A Review represents a user's opinion about a specific restaurant. It includes a star rating and optional comments.
    Attributes:
        id (Integer): A unique identifier for each review.
        star_rating (Integer): A rating from 1 to 5 stars, indicating the customer's satisfaction with the restaurant.
        comments (Text): Optional comments or feedback provided by the customer.
    Relationships:
        customer (Many-to-One): Each review is associated with a single customer who left the review.
        restaurant (Many-to-One): Each review is associated with the restaurant it reviews.

## Dependencies
    * Python 3.9 or higher is recommended for this program as it was developed in version 3.8 but should work on any newer

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

    1. Fork the project on GitHub.
    2. Create a new branch for your feature or bug fix.
    3. Make your changes and commit them.
    4. Push your changes to your fork.
    5. Submit a pull request to the original repository.


## License
MIT License

Copyright (c) 2023 AARON KIPTOO All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,