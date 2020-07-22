def divide(a, b):
    try:
        return a / b
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionErrorError:
        return "Please do not divide with zero"
