# python_program_three.py
#
# Name: Kevin Alcocer
# Date: 09/13/23
# Class: CIT 95

# I modeled the text after a basic customer service robot you hear on the phone. The plan is to use a if-then-else structure as shown in module 6. I defined the second line as "prompt" since I figure I will need to keep referencing that, 
# but not the welcome message as that should only print() at the beginning. 

print("Welcome to the python_program_three contact management system.") 
prompt = print("Please press 1 if you would like to add a new contact. Press 2 if you would like to view all current contacts. Press 3 if you would like to search for a contact by name. Else, press 4 to exit.")
prompt
request = input()

# Here is how the if-then-else structure should more or less look like. I have not defined these values yet but now I atleast have the structure how this program will run/be organized. I also added an exit message so the user knows they have 
# exited the program. The message that is prompted in case anything other than a 1,2,3, or 4 prompts the user to repeat their request and takes them back to the beginning.

if request == "1":
    add_contact()
elif request == "2":
    view_contacts()
elif request == "3":
    search_contact()
elif request == "4":
    print("Thank you for using the python_program_three contact management system! Goodbye.")
else:
    print("I'm sorry, I didn't understand that input.")
    prompt


# I started with an empty list called Contacts. I then wrote out this example below of what a contact should look like:
# Example of a contact: Kevin = {name : Kevin, phone : 714714, email: 714@scccd.edu} <--- these data values need to be input by users

Contacts = []

# "Your program should allow users to add, view, and search for contacts." <- This part of the Assignment Details tells me that the input() function needs to be used in order to add a new contact, phone number, and email:
name = input("Please enter the name of your contact: ")
phone = input("Please enter the phone number of your contact: ")
email = input("Please enter the email of your contact: ")

# Now I have to add these values to a dictionary
new_contact = {'name' : name, 'phone' : phone, 'email' : email}
# print(new_contact)

# Now I need to add New_Contact to the list of empty contacts for every contact that is added. I am thinking some sort of 'for loop' will accomplish this. 
Contacts.append(new_contact)
print(Contacts)

# Instructions from README for reference: 
# Implement a function called add_contact() that takes user input to add a new contact to the contacts list. Ensure that each contact has a unique name.
# Implement a function called view_contacts() that displays the list of all contacts in a user-friendly format.
# Implement a function called search_contact() that takes a name as input and searches for the contact by name. If found, display the contact's details. If not found, display a message indicating that the contact was not found.

# Reading these instructions gives me a nice skeleton/roadmap to work with:
# def add_contact():
# def view_contacts():
# def search_contacts():