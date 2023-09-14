# python_program_three.py
#
# Name: Kevin Alcocer
# Date: 09/13/23
# Class: CIT 95

# I started with an empty list called Contacts. I then wrote out this example below of what a contact should look like:
# Example of a contact: Kevin = {name : Kevin, phone : 714714, email: 714@scccd.edu} <--- these data values need to be input by users

Contacts = []

# "Your program should allow users to add, view, and search for contacts." <- This part of the Assignment Details tells me that the input() function needs to be used in order to add a new contact, phone number, and email:

name = input("Please enter the name of your contact: ")
phone = input("Please enter the phone number of your contact: ")
email = input("Please enter the email of your contact: ")

# Now I have to add these values to a dictionary

New_contact = {'name' : name, 'phone' : phone, 'email' : email}
print(New_contact)

# Now I need to add New_Contact to the list of empty contacts for every contact that is added. I am thinking some sort of 'for loop' will accomplish this. 
Contacts.append(New_contact)
print(Contacts)