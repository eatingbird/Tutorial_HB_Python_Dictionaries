import sys
# your code goes here

def print_restaurant_ratings():
    """Prints restaurants in alphabetical order with their ratings."""

    file_name = sys.argv[1]
    ratings_file = open(file_name)
    ratings = {}

    for line in ratings_file:
        restaurant, rating = line.rstrip().split(":")
        ratings[restaurant] = rating

    # Print restaurants and ratings in alphabetical order
    for restaurant_key in sorted(ratings.keys()):
        print '%s is rated at %s' % (restaurant_key, ratings[restaurant_key])

print_restaurant_ratings()
