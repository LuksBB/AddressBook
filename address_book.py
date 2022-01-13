#title: address_book
#author: Łukasz Boguszko

import time
import os
import re

class Person():
    """This class represents a person in the address book"""
    def __init__(self, name, lastname, phone_number, email):
        self.name = name
        self.lastname = lastname
        self.phone_number = phone_number
        self.email = email

def print_menu():
    """This function prints the menu of the address_book programme"""
    os.system("cls")
    print("How can I help you?\n==========================================")
    print("1. Add a new person to the address book.\n2. Find a person in the adress book.\n3. Change the data for a specific person.\n4. Delete a person from the address book.\n5. Exit.")
    print("==========================================")

people_in_the_address_book = {}

def read_address_book():
    """This function reads the address book from the file"""
    global people_in_the_address_book
    person_data = []
    try:
        with open("book.txt", "r") as book:
            for line in book:
                val = line.split(": ")[1].strip()
                person_data.append(val)
                if(len(person_data) == 4):
                    person = Person(name=person_data[0], lastname=person_data[1], phone_number=person_data[2], email=person_data[3])
                    people_in_the_address_book[f"{person.name} {person.lastname}"] = person
                    person_data.clear()
    except FileNotFoundError as error:
        os.system("cls")
        print("Couldn't find the address book file !\nCreating new empty file..")
        time.sleep(2)
        os.system("nul > book.txt")

def print_person_data(person):
    """This function prints the data for a specific person"""
    print(f"Name: {person.name}\nLastname: {person.lastname}\nPhone Number: {person.phone_number}\nEmail: {person.email}")

def is_number_valid(number):
    """This function checks is the inputed phone number has a valid format"""
    return (len(number) == 9 and number.isnumeric())

def is_email_valid(email):
    """This function checks is the inputed email has a valid format"""
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.fullmatch(regex, email)

read_address_book()          
while(1):
    print_menu()
    option = input("Type \"1\"/\"2\"/\"3\"/\"4\" or \"5\"\nOption: ")
    match option:
        case "1":
            os.system("cls")
            print("Please fill in your data.")
            time.sleep(2)
            os.system("cls")
            name = input("Name: ")
            lastname = input("Lastname: ")
            phone_number = input("Phone number: ")
            while(not is_number_valid(phone_number)):
                print("Please enter the valid phone number !")
                phone_number = input("Phone number: ")
            email = input("Email: ")
            while(not is_email_valid(email)):
                print("Please enter the valid email !")
                email = input("Email: ")
            p = Person(name, lastname, phone_number, email)
            people_in_the_address_book[f"{p.name} {p.lastname}"] = p

            with open("book.txt", "a") as book:
                data = f"Name: {p.name}\nLastname: {p.lastname}\nPhone number: {p.phone_number}\nEmail: {p.email}\n"
                book.write(data)
            print("Done !")
            time.sleep(1)
        case "2":
            os.system("cls")
            name=input("Type in the name: ")
            lastname=input("Type in the lastname: ")
            person = f"{name} {lastname}"
 
            if  person in people_in_the_address_book:
                print_person_data(people_in_the_address_book[person])
                input("Press Enter to continue..")
            else:
                print("No such person in the address book !")
                input("Press Enter to continue..")
           
        case "3":
            os.system("cls")
            name=input("Type in the name: ")
            lastname=input("Type in the lastname: ")
            person = f"{name} {lastname}"

            if  person in people_in_the_address_book:
                print(f"Updating the data for {person}..\n")  
                new_phone_number = input("Phone number: ")
                while(not is_number_valid(new_phone_number)):
                    print("Please enter the valid phone number !")
                    new_phone_number = input("Phone number: ")
                new_email = input("Email: ")
                while(not is_email_valid(new_email)):
                    print("Please enter the valid email !")
                    new_email = input("Email: ")
                people_in_the_address_book[person].phone_number = new_phone_number
                people_in_the_address_book[person].email = new_email
                time.sleep(1)
                print("Data updated")
                input("Press Enter to continue..")
            else:
                print("No such person in the address book !")
                input("Press Enter to continue..")
        case "4":
            os.system("cls")
            name=input("Type in the name: ")
            lastname=input("Type in the lastname: ")
            person = f"{name} {lastname}"

            if  person in people_in_the_address_book:
                people_in_the_address_book.pop(person)
                print(f"{person} deleted from the address book")
                input("Press Enter to continue..")
            else:
                print("No such person in the address book !")
                input("Press Enter to continue..")
        case "5":
            os.system("cls")
            with open("book.txt", "w") as book:
                for person in people_in_the_address_book:
                    data = f"Name: {people_in_the_address_book[person].name}\nLastname: {people_in_the_address_book[person].lastname}\nPhone number: {people_in_the_address_book[person].phone_number}\nEmail: {people_in_the_address_book[person].email}\n"
                    book.write(data)
            print("Closing..")
            time.sleep(1)
            exit()