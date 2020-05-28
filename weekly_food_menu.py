
##################### - WEEKLY FOOD MENU - ###########################################
# "Problem well defined is problem solved" is what the small program
# below demonstrate.
# The current problem is to prepare a weekly food menu from a bunch of food
# options available for breakfast, lunch and dinner. Any special condition like
# one can have only bread or cereal or any other curb products in breakfast also
# achieved through data declaration without much additional code logic.
# This program also shows an usage of generators.
# This is just for demonstration and may have bugs. Feel free to enhance. Cheers!
# AUTHOR - kamaleshpradhan@gmail.com
#####################################################################################

import random


week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
breakfast = [['Bread', 'Cereal', 'Cornflakes', 'Porridge'], 'Omlet', 'Hashbrown', 'Mushroom', 'Boiled Egg', 'Veg Roll']
lunch = ['Rice', 'Curry', 'Vegetables', 'Roti', 'Dessert']
dinner = ['Roti', 'Curry', 'Dal', 'Rice']


def select_food_from(options):
    random.shuffle(options)
    for food in options:
        if type(food) == list:
            random.shuffle(food)
            food = food[0]
        yield food


def get_weekly_food_menu():
    for day in week:
        brf = select_food_from(breakfast)
        lun = select_food_from(lunch)
        din = select_food_from(dinner)

        print('-' * 80)
        print(f'{day} Breakfast - {next(brf)}, {next(brf)}, {next(brf)}, {next(brf)}')
        print(f'{day} Lunch - {next(lun)}, {next(lun)}, {next(lun)}')
        print(f'{day} Dinner - {next(din)}, {next(din)}')


def main():
    get_weekly_food_menu()


if __name__ == "__main__":
    main()
