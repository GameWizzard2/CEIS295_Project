# Name: Christopher H Barfield
# Date: 2024-11-07

import sys
import random
import time

from datetime import date
from LinkedList import LinkedList
from Client import Client
from typing import List

def createClientRecords(newList = []):
    input_file_name = '.\Module_2\ClientData.csv'
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
            newList.append(clt)
        return newList

def appendToLinkedList(numofClients: int, linkedList: 'LinkedList', clientRecords: List['Client']):
    """
    Add clientRecords to the end of a linked list.
    """
    for i in range(numofClients):
        linkedList.add_last(clientRecords[i])

def userContinueInput():
    print("Press \"Enter\" to continue...")
    sys.stdin.read(1)  # Reads one character (like Enter) from standard input


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

print("Name:", "Christopher H Barfield")
print("Date:", date.today())
clientRecords = createClientRecords()
numofClients = len(clientRecords)
funWithLinkedLists = LinkedList()

testLinkedOne(numofClients, funWithLinkedLists, clientRecords)
testLinkedOneContinued(numofClients, funWithLinkedLists)
userContinueInput()
appendToLinkedList(numofClients, funWithLinkedLists, clientRecords)
testLinkedTwo(numofClients, funWithLinkedLists)
userContinueInput()
testLinkedThree(numofClients, funWithLinkedLists, clientRecords)
userContinueInput()