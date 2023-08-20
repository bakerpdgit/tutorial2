colours = ["red", "orange", "yellow", "green", "blue", "purple"]
favourite_colour = "blue"


def add_colour(colour):
    colours.append(colour)


def count_colours():
    print("There are", len(colours), "colours in my list")


def reset_colours():
    colours = ["red", "orange", "yellow", "green", "blue", "purple"]


def set_favourite(colour):
    favourite_colour = colour


def print_favourite():
    print(favourite_colour)


add_colour("indigo")
count_colours()
reset_colours()
count_colours()
set_favourite("turquoise")
print_favourite()
