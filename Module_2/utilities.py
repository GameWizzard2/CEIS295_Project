# built-in
import sys

# Local
from Client import Client
from LinkedList import LinkedList

# Imported
from typing import List

def createClientRecords(newList=None):
    """
    Create client records from a CSV file and store them in a list.

    Args:
        newList (list): A list to store the Client objects. Defaults to an empty list.

    Returns:
        list: A list containing Client objects parsed from the CSV file.
    """
    if newList is None:
        newList = []

    input_file_name = './Module_2/ClientData.csv'
    with open(input_file_name) as infile:
        for line in infile:
            s = line.strip().split(',')
            client_id = int(s[0])  # Convert the default string to an int
            f_name = s[1]
            l_name = s[2]
            phone = s[3]
            email = s[4]
            
            # Create a client object using the data from the file
            clt = Client(client_id, f_name, l_name, phone, email)
            
            # Add the client object to the list
            newList.append(clt)
    return newList

def appendToLinkedList(numofClients: int, linkedList: LinkedList, clientRecords: List[Client]):
    """
    Append client records to the end of a LinkedList.

    Args:
        numofClients (int): The number of Client objects to append.
        linkedList (LinkedList): The LinkedList to append records to.
        clientRecords (list of Client): A list containing Client objects.

    Returns:
        LinkedList: The updated LinkedList containing appended Client records.
    """
    for i in range(numofClients):
        linkedList.add_last(clientRecords[i])
    return linkedList

def userContinueInput():
    """
    Pause execution and wait for user input.

    Prints:
        A message asking the user to press "Enter".
    """
    print('Press "Enter" to continue...')
    sys.stdin.read(1)
