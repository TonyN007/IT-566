#Create an Inventory system for the Application

from Inventory import Inventory
from subprocess import call
import os


class InventoryApp():

	def __init__(self):
		"""Initialize object."""
		# Constants
		self.NEW_INVENTORY='1'
		self.LOAD_INVENTORY='2'
		self.PACKAGE_INFORMATION='3'
		self.ARRIVAL_AND_PICKUP='4'
		self.ADD_ITEMS='5'
		self.SAVE_INVENTORY='6'
		self.EXIT='9'
		# Fields
		self.menu_choice = 1
		self.keep_going = True
		self.inventory = Inventory()
		pass

	def clear_screen(self):
		try:
				os.system('clear')
		except Exception:
				os.system('cls')


	def display_menu(self):
		"""Display menu."""
		print('\t\t Package Inventory Application')
		print()
		print('\t\t1. New Inventory')
		print('\t\t2. Load Inventory')
		print('\t\t3. Package Information')
		print('\t\t4. Arrival and Pickup')
		print('\t\t5. Add Items')
		print('\t\t6. Save Inventory')
		print('\t\t9. Exit')
		print()

	def process_menu_choice(self):
		"""Process menu choice and execute corrensponding methods."""
		self.menu_choice = input('Please enter menu item number: ')
		match self.menu_choice:
			case self.NEW_INVENTORY:
				self.new_inventory()
			case self.LOAD_INVENTORY:
				self.load_inventory()
			case self.PACKAGE_INFORMATION:
				self.package_information()
			case self.ARRIVAL_AND_PICKUP:
				self.arrival_and_pickup()
			case self.ADD_ITEMS:
				self.add_items()
			case self.SAVE_INVENTORY:
				self.save_inventory()
			case self.EXIT:
				if __debug__:
					print('Goodbye!')
				self.keep_going = False
				self.clear_screen
			case _:
				print('Invalid')

	def new_inventory(self):
		"""Create new inventory."""		
		self.inventory.new_inventory()

	def load_inventory(self):
		"""Load inventory from file."""
		self.inventory.load_inventory()

	def package_information(self):
		"""Package Information."""
		self.clear_screen()
		self.inventory.package_information()
		self.clear_screen()

	def arrival_and_pickup(self):
		"Adds pickup and arrival date"
		self.clear_screen()
		self.inventory.arrival_and_pickup()
		self.clear_screen()

	def save_inventory(self):
		"""Save inventory to file."""
		self.inventory.save_inventory()

	def add_items(self):
		"""Add items to inventory."""
		keep_going = 'y'
		while keep_going[0] == 'y':
			item_name = input('Item Name: ')
			item_count = input('Item Count: ')
			self.inventory.add_item(item_name, item_count)
			keep_going = input('Add another? (y/n): ')

	def start_application(self):
		"""Start the applications."""
		# Clear Screen
		self.clear_screen()
		while self.keep_going:
			self.display_menu()
			self.process_menu_choice()
			
					



		

