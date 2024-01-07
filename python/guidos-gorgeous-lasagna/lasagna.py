"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(lasagna_layers):
    """Calculate the preparation times based on many layers the lasagna has.

    :param lasagna_layers: int - layers of the lasagna.
    :return: int - total bake time (in minutes) to all layers.

    Function that takes the layers on the lasagna as an argument and 
    returns how many minutes it will take to the lasagna to be ready.
    """
    return PREPARATION_TIME * lasagna_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time in minutes based on bake time and number of the layers.

    :param number_of_layers: int - number of layers that the lasagna has.
    :param elapsed_bake_time: int - elapsed bake time of the lasagna.
    :return: int - total elapsed bake time (in minutes).

    Function that takes the elapsed bake time and the number of layers and returns and sum both to give the total elapses time.
    """
    preparation_layers_total_time= preparation_time_in_minutes(number_of_layers)
    return elapsed_bake_time + preparation_layers_total_time
