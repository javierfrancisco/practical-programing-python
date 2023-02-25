# Python comes with many built-in functions that perform common operations.
# one example:
print(abs(-9))

print(abs(3.3))

day_temperature = 3
night_temperature = 10
print(abs(day_temperature - night_temperature))

# Here are the rules to executing a function call:
# 1. Evaluate each argument one at a time, working from left to right.
# 2. Pass the resulting values into the function.
# 3. Execute the function. When the function call finishes, it produces a value.

# because functions calls produce values, they can be used in expressions:

print(abs(-7) + abs(3.3))

# We can also use function calls as arguments to other functions:

print(pow(abs(-2), round(4.3)))

# Some of the most useful built-in functions are ones that convert from one type to another.
# Type names int and float can be used as functions:

print(int(34.6))

print(int(-4.3))

print(float(21))

# function help shows documentation for any function:

# help(abs)

# help(round)

# Another built-in function is round, which rounds a floating-point number to the nearest integer:
print(round(3.8))

print(round(3.3))

print(round(3.5))

print(round(-3.3))

print(round(-3.5))


def convert_to_celcius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


print("Time to call a function: using convert_to_celcius(80)")


# Quadratic polynomial ax2 + bx + c
def quadratic(a, b, c, x):
    first = a * x * x
    second = b * x
    third = c
    return first + second + third


print("Calling a quadratic polynomial function: using quadratic(2, 3, 4, 0.5)")

quadratic(2, 3, 4, 0.5)

print(convert_to_celcius(80))


def days_difference(day1: int, day2: int) -> int:
    """Return the number of days between day1 and day2, which are
    both in range 1-365 (thus indicating the day of the year).

    days_difference(200, 224)
    24
    days_difference(50, 50)
    0
    days_difference(100, 99)
    -1
    """
    return day2 - day1


print(days_difference(200, 224))


def get_weekday(current_weekday: int, days_ahead: int) -> int:
    """Return which day of the week it will be days_ahead days from
    current_day.

    current_weekday is the current day of the week and is in the rante
    1-7, indicating whether today is Sunday (1), Monday (2),
    ..., Saturday (7).

    days_ahead is the number
    """
    return (current_weekday + days_ahead) % 7


def get_birthday_weekeday(current_weekday: int, current_day: int,
                          birthday_day: int) -> int:
    """Return the day of the week it will be on birthday_day,
    given that the day of the week is current_weekday and the
    day of the year is current_day.

    current_weekday is the current day of the week and is in
    the range 1-7, indicating whether today is Sunday (1),
    Monday (2), ..., Saturday (7).

    current_day and birthday_day are both in the range 1-365.
    """
    days_diff = days_difference(current_day, birthday_day)
    birthday_weekday = get_weekday(current_weekday, days_diff)

    return birthday_weekday


print(get_birthday_weekeday(5, 3, 4))
