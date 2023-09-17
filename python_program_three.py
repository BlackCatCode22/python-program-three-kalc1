# python_program_three.py
#
# Name: Kevin Alcocer
# Date: 09/13/23
# Class: CIT 95

# I modeled the text after a basic customer service robot you hear on the phone. The plan is to use a if-then-else structure as shown in module 6. I defined the second line as "prompt" since I figure I will need to keep referencing that, 
# but not the welcome message as that should only print() at the beginning. 

# Here is how the if-then-else structure should more or less look like. I have not defined these values yet but now I atleast have the structure how this program will run/be organized. I also added an exit message so the user knows they have 
# exited the program. The message that is prompted in case anything other than a 1,2,3, or 4 prompts the user to repeat their request and takes them back to the beginning.
# I added an option to add another contact.
# Using the same logic from the while-loop controlling the main menu, I was able to re-direct the user back to the main menu after choosing no or prompting them to continue adding another contact incase of an invalid input. 

Contacts = []

def add_contact(): 
    name = input("Please enter the name of your contact: ")
    phone = input("Please enter the phone number of your contact: ")
    email = input("Please enter the email of your contact: ")
    new_contact = {'name' : name, 'phone' : phone, 'email' : email}
    Contacts.append(new_contact)
    print(new_contact['name'] + " has been added to your contacts list.")
    add_another = input("Would you like to add another contact? Enter yes or no. ")
    if add_another == "yes":
        add_contact()
    elif add_another == "no":
        print("Returning to main menu:")
    else:
        print("I'm sorry, I didn't understand that input.")  
        add_another = input("Would you like to add another contact? Enter yes or no. ")
 
# I first started with simply printing out the list of Contacts. It wasn't very readable as it simply printed out the information in a dictionary format. My first attempt at listing all the contacts in a more readable format will use iteration. 
    
def view_contacts():
    for i in Contacts:
        print(i['name'])
 
# My first instinct is to use iteration again as in the view_contacts() function but instead of just printing each name as it cycles through the list, the program will only print out names and their email/phone number if it matches the user's input.
def search_contact():
    search_name = input("Please type the name of the contact you are searching for: ")
    for i in Contacts:
        if search_name == i['name']:
            print(i['name'] + " is currently in your contacts list with the following phone number and email:")
            print(i['phone'])
            print(i['email'])
        else:
            print("That contact does not exist.")
              
             
def main_menu():
    if prompt == "1":
        add_contact()
    elif prompt == "2":
        view_contacts()
    elif prompt == "3":
        search_contact()
    else:
        print("I'm sorry, I didn't understand that input.") 
        

# I started with an empty list called Contacts. I then wrote out this example below of what a contact should look like:
# Example of a contact: Kevin = {name : Kevin, phone : 714714, email: 714@scccd.edu} <--- these data values need to be input by users

# Contacts = [] <--- I moved this to the beginning of the if-then-else structure so it would run before anything is done with it.

# I already figured out how to add a new contact so I just definined it below. I also added an else-if statement to check if the name has already been entered into the system to ensure each contact has a unique name. 
# # "Your program should allow users to add, view, and search for contacts." <- This part of the Assignment Details tells me that the input() function needs to be used in order to add a new contact, phone number, and email:
# def add_contact(): 
    #name = input("Please enter the name of your contact: ")
    #if name == new.contact['name']:
    #    print("That contact already exists. Please enter a different name.")
    #    add_contacts()
    #else:
    #    phone = input("Please enter the phone number of your contact: ")
    #    email = input("Please enter the email of your contact: ")
    #    new_contact = {'name' : name, 'phone' : phone, 'email' : email}
    #    Contacts.append(new_contact) 
    # ^^^ this entire function was moved to the top once I ran the code and realized this needed to run before the main if-then-else structure

# Now I have to add these values to a dictionary
# new_contact = {'name' : name, 'phone' : phone, 'email' : email}
# print(new_contact)

# Now I need to add New_Contact to the list of empty contacts for every contact that is added. I am thinking some sort of 'for loop' will accomplish this. 
# Contacts.append(new_contact)

# print(Contacts)

# Instructions from README for reference: 
# Implement a function called add_contact() that takes user input to add a new contact to the contacts list. Ensure that each contact has a unique name.
# Implement a function called view_contacts() that displays the list of all contacts in a user-friendly format.
# Implement a function called search_contact() that takes a name as input and searches for the contact by name. If found, display the contact's details. If not found, display a message indicating that the contact was not found.

# Reading these instructions gives me a nice skeleton/roadmap to work with:
# def add_contact():
# def view_contacts():
# def search_contacts():
# I first attempted to write this as while prompt != "4" but I kept getting error messages. For some reason this "while not" works as intended. 

print("Welcome to the python_program_three contact management system.") 
prompt = input("Please press 1 if you would like to add a new contact. Press 2 if you would like to view all current contacts. Press 3 if you would like to search for a contact by name. Else, press 4 to exit: ")  
while not prompt == "4":
    main_menu()
    prompt = input("Please press 1 if you would like to add a new contact. Press 2 if you would like to view all current contacts. Press 3 if you would like to search for a contact by name. Else, press 4 to exit: ")  
print("Thank you for using the python_program_three contact management system! Goodbye.")