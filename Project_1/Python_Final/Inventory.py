"""Implements Home Inventory data structures and operations."""

import json
from datetime import date
import string
import random

class Inventory():
    """Implements Home Inventory data structures and operations."""

    def __init__(self):
        """Initialize Home Inventory object."""
        self._initialize_inventory_dictionary()
        
    def new_inventory(self):
        """Initialize new dictionary to store inventory data."""
        if (self.dictionary != None) and (bool(self.dictionary)):
            user_input = input("Save current inventory? (y/n): ")
            match user_input.lower():
                case 'y':
                    self.save_inventory()
                    self._initialize_inventory_dictionary()
                case 'n':
                    self._initialize_inventory_dictionary()
                case _:
                    self._initialize_inventory_dictionary()
        else:
            self._initialize_inventory_dictionary()

    def load_inventory(self):
        """Load inventory from file."""
        try:
            file_path = self._get_file_path()
            with open(file_path, 'r', encoding='UTF-8') as f:
                self.dictionary = json.loads(f.read())
        except OSError:
            print('File does not exist. Please try again.')

    def save_inventory(self):
        """Save inventory to file."""
        if self.dictionary != None:
            file_path = self._get_file_path()
            with open(file_path, 'w', encoding='UTF-8') as f:
                f.write(json.dumps(self.dictionary))

    def package_information(self):
        """Information related to Package"""
        name = input('Enter Full Name: ')
        letters = list(string.ascii_uppercase)
        digits = list(string.digits)
        print(f"This package belongs to: ",name)
        print(f"Place package in: ",'('+random.choice(string.ascii_uppercase) 
        +random.choice(string.digits)+')')
        print("")
        name = input('Enter Full Name: ')
        print(f"This package was picked up by: ",name)
        input('Enter any key to continue... ')


    def add_item(self, item_name, item_count):
        assert self.dictionary != None
        self.dictionary['items'].append({'item': item_name, 'count': int(item_count)})

    def arrival_and_pickup(self):
        "Arrival and Pickup Date"
        month = int(input('Enter month: '))
        day = int(input('Enter day: '))
        year = int(input('Enter year: '))
        d = date(year, month, day)
        print("Package arrived on =", d)
        month = int(input('Enter month: '))
        day = int(input('Enter day: '))
        year = int(input('Enter year: '))
        d = date(year, month, day)
        print("Package was picked up on", d)
        input('Enter any key to continue...')

    def _get_file_path(self):
        """Get flle path from user."""
        f_path = input("Please enter path and filename: ")
        return f_path

    def _initialize_inventory_dictionary(self):
        if __debug__:
            print("Initializing new Inventory...")
        self.dictionary = {}
        self.dictionary['type'] = 'Inventory'
        self.dictionary['date'] = date.today().isoformat()
        self.dictionary['items'] = []
        if __debug__:
            print("New Inventory Initialized")