# defining a simple function

def addFunction (a, b):
    return a + b

def maximum(lyst):
    """ Function returns the max value of the list"""
    return max(lyst)

def average(lyst):
    ''' Take all the values of a list and returns the average value for the variables'''
    theSum = 0
    for number in lyst:
        theSum += number
    return theSum / len(lyst)

def odd(x):
    '''This function will return odd or false otherwise'''
    if x % 2 == 1:
        return True
    else:
        return False
