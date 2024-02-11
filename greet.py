#!/usr/bin/python3
def greet(name):
    
    if not isinstance(name, str):
        raise TypeError('Name must be a string.')
    
    greeting = f'Hello, {name}! How are you today?'
    return greeting

