""" This module contains functions for conversions from celsius and fahrenheit """
def convertToCelsius (fahrenheit):
    """ Accepts degrees Fahrenheit and returns Celsius """
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def convertToFahrenheit (celsius):
    """ Accepts degrees in Celcius and returns Fahrenheit """
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

