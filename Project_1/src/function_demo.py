''' Function demo module.

    Demonstrate basic function concepts
'''
__all__ = ['greet_person_by_name']

def print_greeting():
    print('Hello, Tony')

def greet_person_by_name(name):
    print(f'Hello {name}')

def _private_function():
    pass