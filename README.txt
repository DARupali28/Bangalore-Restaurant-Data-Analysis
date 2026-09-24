# Bangalore Restaurant Data Analysis

## Project Overview

This project analyzes a synthetic Bangalore restaurant dataset using Python, Pandas, MySQL, and Matplotlib.

The project explores restaurant locations, cuisines, ratings, votes, menu items, online ordering, and table booking using SQL analysis and Python visualizations.

## Project Objective

The objective of this project is to:

- Analyze restaurant distribution across locations
- Identify popular cuisines
- Analyze restaurant ratings and votes
- Compare menu sizes across restaurants
- Analyze online ordering and table booking
- Visualize important patterns in the data

## Technologies Used

- Python
- Pandas
- MySQL
- Matplotlib
- Jupyter Notebook
- SQL

## Database Structure

| Table | Description |
|---|---|
| restaurants | Restaurant details, ratings, votes, cost and services |
| locations | Location and geographic information |
| cuisines | Cuisine master data |
| restaurant_cuisines | Restaurant-cuisine relationships |
| menu | Menu items and prices |
| reviews | Restaurant review information |

## Relationships:
restaurants.location_id -> locations.location_id
restaurant_cuisines.restaurant_id -> restaurants.restaurant_id
restaurant_cuisines.cuisine_id -> cuisines.cuisine_id
menu.restaurant_id -> restaurants.restaurant_id
reviews.restaurant_id -> restaurants.restaurant_id


## Project Workflow

1. Load CSV data using Pandas
2. Create and connect to MySQL database
3. Import data into MySQL tables
4. Inspect table structures and record counts
5. Perform data quality checks
6. Analyze data using SQL
7. Retrieve SQL results using Python
8. Create visualizations using Matplotlib
9. Summarize key insights

## Analysis Performed

The project answers questions such as:

- How many restaurants are in the dataset?
- Which locations have the most restaurants?
- Which cuisines are most popular?
- What is the average restaurant rating?
- Which restaurants have the highest number of votes?
- Which restaurants have the most menu items?
- How many restaurants offer online ordering?
- How many restaurants offer table booking?
- How are restaurant ratings distributed?
- What is the relationship between ratings and votes?

## Visualizations

The project includes:

- Number of Restaurants by Location
- Top 10 Cuisines by Number of Restaurants
- Top 10 Cuisines by Average Rating
- Top 10 Restaurants by Votes
- Top 10 Restaurants by Number of Menu Items
- Distribution of Restaurant Ratings
- Restaurant Rating vs Votes

## Key Insights

- The dataset contains 100 restaurants across 20 locations.
- Jayanagar has the highest number of restaurants.
- Andhra is the most represented cuisine.
- The average restaurant rating is 3.97.
- Online ordering is available at most restaurants in the dataset.
- The Diner has the highest number of votes.
- Urban Tadka and Grand Table have the highest menu-item counts among the top restaurants analyzed.

## Data Disclaimer

This project uses synthetic practice data created for learning Python, Pandas, and SQL.

It is not real Zomato data and does not represent actual customer, restaurant, or order activity.
