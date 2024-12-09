from SortingAlgo.Quicksort import Quicksort
from typing import List
import logging
import sys

#Local
from Client import Client
from .ArrayList import ArrayList




def appendToArray(numofClients: int, arrayList: 'ArrayList', clientRecords: List['Client']):
    """
    Add clientrecords to an array list Tests.

    This function iterates through the provided clientRecords list and appends the specified 
    number of Client objects to the end of the provided ArrayList instance. It is designed 
    to test the performance of adding records to the ArrayList.
    
    Args:
        numofClients (int): The number of Client objects to be added to the ArrayList.
        arrayList (ArrayList): An instance of the ArrayList class representing the data structure 
                           to which Client objects will be added.
        clientRecords (list): A list containing Client objects to be added to the ArrayList.

    Returns:
        None
       
    """
    for i in range(numofClients):
        arrayList.append(clientRecords[i])

def remove_from_array(numofClients: int, arrayList: 'ArrayList'):
    """
    Remove Client objects from the front of an existing ArrayList, one at a time.

    Args:
        numofClients (int): The number of Client objects to be added to the ArrayList.
        arrayList (ArrayList): An instance of the ArrayList class representing the data structure 
                           to which Client objects will be added.

    Returns:
        None
    """
    for i in range(numofClients):
        arrayList.remove_at(0)

def create_client_records():
    """
    Reads client data from a CSV file and creates client objects.

    This function reads each line from 'ClientData.csv', extracts client information, 
    and creates a Client object for each record. The created client objects are appended 
    to the provided clientRecords list.

    Args:
        clientRecords (list): A list to store Client objects created from the CSV data.

    Returns:
        None
    """
    clientRecords = []
    input_file_name = 'ClientData.csv'
    with open(input_file_name) as infile:
        for line in infile:
            s = line.split(',')
            client_id = int(s[0])  # convert the default string to an int
            f_name = s[1]
            l_name = s[2]
            phone = s[3]
            email = s[4]
            
            # create a client object using the data from the file
            clt = Client(client_id, f_name, l_name, phone, email)
            
            # add the client object to the list
            clientRecords.append(clt)
        return clientRecords

# working on reformating this to only call to create an array, and check for an existing one.
def createArray():
    """
    Returns:
        clientRecords (list):

        """
    
    clientRecords = []
    clientRecords = create_client_records()
    Quicksort.sort(clientRecords) #FIXME make this an optional call for user.
    array = ArrayList()
    numofClients = len(clientRecords)


    for i in range(numofClients):
        array.append(clientRecords[i])

    return numofClients, array, clientRecords 

def checkForExistingArray(numofClients: int, existingArray = None):
    if not existingArray:
        logging.debug("The array is empty or not provided. Create an array in the menu.")
        return False
    elif numofClients == 0:
        logging.debug("Array exists but has no clients. Create an array in the menu.")
        return False
    else:
        logging.info("Using pre-existing array data!")
        return True