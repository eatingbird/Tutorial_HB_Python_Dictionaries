import sys
# your code goes here

ratings = {}


def get_ratings_from_file(ratings):
    """Prints restaurants in alphabetical order with their ratings."""

    file_name = sys.argv[1]
    ratings_file = open(file_name)

    for line in ratings_file:
        restaurant, rating = line.rstrip().split(":")
        ratings[restaurant] = int(rating)


def print_restaurant_ratings(ratings):
    """doc string needed"""

    # Print restaurants and ratings in alphabetical order
    for restaurant in sorted(ratings.keys()):
        print '%s is rated at %d' % (restaurant, ratings[restaurant])


def get_ratings_from_user(ratings):
    """doc"""

    print "Type 'q' to quit."

    prompt_user = True

    while prompt_user:
 
        restaurant = raw_input("Enter the name of the restaurant: ")
        rating = int(raw_input("Enter the rating of the restaurant: "))

        restaurant = restaurant[0].upper() + restaurant[:-1]
        ratings[restaurant] = rating

        user_choice = raw_input("Do you want to add another restaurant? y/n ").lower()


        if user_choice is 'y':
            continue
        elif user_choice is 'n':
            prompt_user = False
        else:
            print "The answer was supposed to be y or n. We will print the result thus far."
            prompt_user = False


get_ratings_from_file(ratings)
get_ratings_from_user(ratings)
print
print_restaurant_ratings(ratings)
