
#Following the function design recipe, define a function that has one parameter,
# a number, and returns that number tripled

def tripled(input: int) -> int:
    """Returns the input value times three."""
    return input * 3


#  Following the function design recipe, define a function that has two parameters,
#  both of which are numbers, and returns the absolute value of the difference of the two.
#  Hint: Call built-in function abs

def get_input_difference(input_1: int, input_2: int) -> int:
    """Returns the difference between input_1 and input_2"""
    return abs(input_1 - input_2)


# Following the function design recipe, define a function that has one parameter,
#  a distance in kilometers, and returns the distance in miles. 
# (There are 1.6 kilometers per mile.)

def convert_to_miles(input_kilometers: int) ->  int:
    """Converts input_kilometers into miles given there are 1.6 kilometers per mile."""
    return input_kilometers * 1.6

# Following the function design recipe, define a function that has three parameters,
#  grades between 0 and 100 inclusive, and returns the average of those grades.

def get_average(input_1: int, input_2: int, input_3: int) -> int:
    """Precondition: input_1, input_2, input_3 must be between 0 and 100 inclusive
    
    Returns the average between 3 inputs"""
    return (input_1 + input_2 + input_3) / 3


# Following the function design recipe, define a function that has four parameters, 
# all of them grades between 0 and 100 inclusive, and returns the average of the best 3 of those grades.
#  Hint: Call the function that you defined in the previous exercise.

def get_best_average(input_1: int, input_2: int, input_3: int, input_4: int) -> int:
    """Precondition: input_1, input_2, input_3 and input_4 must be between 0 and 100 inclusive
    Returns the average of the best 3 grades.
    """
    int_list = []
    int_list.append(input_1)
    int_list.append(input_2)
    int_list.append(input_3)
    int_list.append(input_4)
    sorted(int_list)
    return get_average(int_list[0], int_list[1], int_list[2])


print(get_average(10,10,10))
print("the average of the 3 out 4 best grades is:", get_best_average(10,10,10, 2))


def weeks_elapsed(day1, day2): 
    """ (int, int) -> int
    day1 and day2 are days in the same year. Return the number of full weeks
    that have elapsed between the two days.
    >>> weeks_elapsed(3, 20)
    2
    >>> weeks_elapsed(20, 3)
    2
    >>> weeks_elapsed(8, 5)
    >>> weeks_elapsed(40, 61)
    """
    return (abs(day1 - day2) / 7)



#Consider this code:
def square(num):
    """ (number) -> number
    Return the square of num.
    >>> square(3)
    9
    """
    return num * num