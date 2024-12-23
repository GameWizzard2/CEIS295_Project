# Name: Christopher H Barfield
# Date: 2024-11-16

from time import strftime

class Call:
    """
    The Call class represents a record of a customer's call, including client ID, 
    customer name, phone number, call date, and call time.
    """

    def __init__(self, client_id=0, customer_name="Unknown", customer_phone="Unknown"):
        self.__client_id = client_id
        self.__customer_name = customer_name
        self.__customer_phone = customer_phone
        self.__call_date = strftime("%m/%d/%Y")
        self.__call_time = strftime("%H:%M")

    # __str__() method is automatically called when you print the object
    def __str__(self):
        # Split customer_name into first_name and last_name if provided
        names = self.__customer_name.split()
        last_name = names[-1] if len(names) > 1 else "Unknown"
        first_name = " ".join(names[:-1]) if len(names) > 1 else self.__customer_name
        return f"ID: {self.__client_id} \nLast Name: {last_name} \nFirst Name:{first_name} \nPhone:{self.__customer_phone} \nCall Date/Time: {self.__call_date} @ {self.__call_time} "

    # Getters and setters None
    