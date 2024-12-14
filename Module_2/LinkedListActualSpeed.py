# Name: Christopher H Barfield
# Date: 2024-11-07

# local
from LinkedList import LinkedList
from Client import Client
from utilities import (
     appendToLinkedList,
)

# Built-in
from datetime import date
import random
import time

# Imported
from typing import List


def testLinkedOne(numofClients: int, linkedList: 'linkedList', clientRecords: List['Client']):
        """
    Desciption: TODO

    Args:
        numofClients (int): The number of Client objects to be added to the LinkedList.
        linkedList (LinkedList): An instance of the LinkedList class representing the data structure 
                           to which Client objects will be added.

    Returns:
        None
        """
        startTime = time.time()
        appendToLinkedList(numofClients, 
                           linkedList,
                           clientRecords
                           )
        endTime = time.time()
        elapsedTime = endTime - startTime
        print(f"\n1.\tTime taken to remove {numofClients} client records from LinkedList: {elapsedTime:.6f} seconds")

def testLinkedOneContinued(numofClients: int, linkedList: 'LinkedList'):
    """
    Desciption: TODO

    Args:
        numofClients (int): The number of Client objects to be added to the LinkedList.
        linkedList (LinkedList): An instance of the LinkedList class representing the data structure 
                           to which Client objects will be added.

    Returns:
        None

    """
    startTime = time.time()
    for i in range(numofClients):
        linkedList.remove_first()
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f"\n1-2.\tTime taken to remove {numofClients} client records from LinkedList: {elapsedTime:.6f} seconds")

def testLinkedTwo(numofClients: int, linkedList: 'LinkedList'):
    """

    Args:
        numofClients (int): The number of Client objects present in the LinkedList.
        linkedList (LinkedList): An instance of the LinkedList class representing the data structure 
                               from which client records will be searched.

    Returns:
        None
    """
    # How long does it take to display 1000 random records?
    startTime = time.time()
    for i in range(1000):
        smallest_id = 100000
        largest_id = smallest_id + numofClients
        random_num = random.randint(smallest_id, largest_id)
        print(linkedList.search(Client(random_num)))



    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f"\n2.\tTime taken to search for {numofClients} random client records: {elapsedTime:.6f} seconds")

def testLinkedThree(numofClients: int, linkedList: 'LinkedList', clientRecords: List['Client'], ):
    """
    Description: TODO

    Args:
        numofClients (int): The number of Client objects to be added, displayed, and removed from the LinkedList.
        linkedList (LinkedList): An instance of the LinkedList class representing the data structure 
                               in which client records will be added, displayed, and removed.
        clientRecords (list of Client): A list containing Client objects to be added to the LinkedList.

    Returns:
        None
    """
    startTime = time.time()
    # append to LinkedList.
    appendToLinkedList(numofClients, linkedList, clientRecords)

    # Display 1000 random records.
    for i in range(1000):
        smallest_id = 100001
        largest_id = smallest_id + numofClients
        random_num = random.randint(smallest_id, largest_id)
        print(linkedList.search(Client(random_num)))
    
    # Delete 1000 random records
    for i in range(1000):
        smallestId = 100001
        largestId = smallestId + numofClients
        random_num = random.randint(smallest_id, largest_id)
        print(linkedList.search(Client(random_num)))
    

    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f"\n3.\tTime taken to add {numofClients}, and then display and remove 1000 random client records: {elapsedTime:.6f} seconds")
