#Name: Christopher Barfield
#Date:  11/23/2024

class Client:
    """
    The Client class represents an individual client with attributes such as client ID, 
    first name, last name, phone number, and email address.

    This class includes comparison methods for sorting and equality checks, along with string 
    representation and standard getter and setter methods for each attribute.
    """
    def __init__(self, client_id=0, first_name="Unknown", last_name="Unknown", phone="Unknown", email="Unknown"):
        self.__client_id = client_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__phone = phone
        self.__email = email

    
    
    def __lt__(self, other):
        # __lt__ means "less than" and it must return a boolean
        this_full_name = f"{self.__last_name} {self.__first_name}"
        other_full_name = f"{other.__last_name} {other.__first_name}"

        return this_full_name < other_full_name

    def __eq__(self, other):
        # __eq__ means "equals" and it must return a boolean
        return self.__client_id == other.__client_id
    
    def __le__(self, other):
        # __le__ means "less than or equal to" and it must return a boolean
        this_full_name = f"{self.__last_name} {self.__first_name}"
        other_full_name = f"{other.__last_name} {other.__first_name}"

        return this_full_name < other_full_name

    
    def __str__(self):
        # __str__() method is automatically called when you print the object
        return f"{self.__last_name},{self.__first_name}"