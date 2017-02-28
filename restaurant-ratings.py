import sys
# your code goes here

def print_ratings():
    file_name = sys.argv[1]
    ratings_file = open(file_name)
    restaurant_ratings = {}

    for line in ratings_file:
        restaurant, rating = line.rstrip().split(":")
        restaurant_ratings[restaurant] = rating

    for restaurant_key in sorted(restaurant_ratings.keys()):
        print '%s is rated at %s' % (restaurant_key, restaurant_ratings[restaurant_key])

print_ratings()
