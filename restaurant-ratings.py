import sys
# your code goes here

ratings = {}


def get_ratings_from_file(ratings):
    """Set restaurants and ratings from file as key value pairs."""

    file_name = sys.argv[1]
    ratings_file = open(file_name)

    for line in ratings_file:
        restaurant, rating = line.rstrip().split(":")
        ratings[restaurant] = int(rating)


def print_restaurant_ratings(ratings):
    """Prints restaurants in alphabetical order with their ratings."""

    for restaurant, rating in sorted(ratings.items()):
        print '%s is rated at %d' % (restaurant, rating)


def get_ratings_from_user(ratings):
    """Prompts users for restaurants and ratings.

    Sets restuarant and ratings as key value pairs to supplied dictionary.
    """

    restaurant = raw_input("Enter the name of the restaurant: ")
    rating = int(raw_input("Enter the rating of the restaurant: "))

    restaurant = restaurant[0].upper() + restaurant[:-1]
    ratings[restaurant] = rating


def prompt_user(ratings):
    """ This runs the restaurant-ratings program."""

    while True:

        get_ratings_from_user(ratings)

        # Ask user if they want to keep entering restaurants and ratings
        user_choice = raw_input("Do you want to add another restaurant? y/n ").lower()

        if user_choice == 'y':
            continue
        elif user_choice == 'n':
            print_result = raw_input("Do you want to print the result? y/n ").lower()
            if print_result == 'y':
                print
                print_restaurant_ratings(ratings)
                break
            elif print_result == 'n':
                break
            else:
                print "Restaurants will not be printed."
                break
        else:
            print "Invalid input. Program will quit without printing."
            break



get_ratings_from_file(ratings)
prompt_user(ratings)
