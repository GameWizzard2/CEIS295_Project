#Name: Christopher Barfield
#Date:  11/2/2024

from Array.ArrayList import ArrayList #FIXME Find out if you can put this in __init__.py in the folder Array??? Otherwise it has to be called like this?
from Client import Client
from SortingAlgo.Quicksort import Quicksort
from datetime import date
from typing import List
import logging
import time
import random
import sys

# Consdier this addRecords()
def testNumberOne(numofClients, arrayList, clientRecords):
    """
    Tests the time taken to add a specified number of Client objects to the end of an ArrayList.

    This function simulates the process of accepting jobs at the end of a line and processing 
    them from the front, evaluating the performance of the ArrayList data structure. It measures 
    and logs the time taken to add Client objects to the ArrayList, which automatically appends 
    new records at the end. The recorded time can be used to populate a spreadsheet row 
    corresponding to the "Add many records to end of data structure" scenario.

     Args:
        numofClients (int): The number of Client objects to be added to the ArrayList.
        arrayList (ArrayList): An instance of the ArrayList class representing the data structure 
                           to which Client objects will be added.
        clientRecords (list): A list containing Client objects to be added to the ArrayList.

    Returns:
        None
    """
    startTime = time.time()
    appendToArray(numofClients, arrayList, clientRecords)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f"\n1.\tTime taken to add {numofClients} client records to ArrayList: {elapsedTime:.6f} seconds")

# Consider this removeFromStart()
def testNumberOneContinued(numofClients: int, arrayList: 'ArrayList'):
    """
    Tests the time taken to remove Client objects from the front of an existing ArrayList, one at a time.

    This function measures the performance of removing Client objects from the front of an 
    ArrayList instance, simulating the process of pulling records one by one. The time taken 
    for the operation is recorded and can be used for performance analysis in the 
    "Pull all records off front of data structure" scenario for an Excel table or report.

    Args:
        numofClients (int): The number of Client objects to be added to the ArrayList.
        arrayList (ArrayList): An instance of the ArrayList class representing the data structure 
                           to which Client objects will be added.

    Returns:
        None

    """
    startTime = time.time()
    for i in range(numofClients):
        arrayList.remove_at(0)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f"\n1-2.\tTime taken to remove {numofClients} client records from ArrayList: {elapsedTime:.6f} seconds")

# Consider this displayAThousandRandomRecords()
def testNumberTwo(numofClients: int, arrayList: 'ArrayList'):
    """
     Tests the time taken to search for and display random client records from an ArrayList.

    This function simulates a customer service scenario where client records need to be retrieved 
    quickly and at random. It measures the time taken to search for 1000 random client records 
    within an ArrayList. The recorded time can be used for performance analysis in the 
    "Display random records" scenario for an Excel table or report. Before searching, the function 
    assumes that all client records have already been added to the ArrayList.

    Args:
        numofClients (int): The number of Client objects present in the ArrayList.
        arrayList (ArrayList): An instance of the ArrayList class representing the data structure 
                               from which client records will be searched.

    Returns:
        None
    """
    # How long does it take to display 1000 random records?
    startTime = time.time()
    for i in range(1000):
        smallest_id = 100001
        largest_id = smallest_id + numofClients
        random_num = random.randint(smallest_id, largest_id)
        print(arrayList.search(Client(random_num))) #FIXME allow user to choose.
        #print(arrayList.search_sorted(Client(random_num)))


    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f"\n2.\tTime taken to search for {numofClients} random client records: {elapsedTime:.6f} seconds")
    

def testNumberThree(numofClients: int, arrayList: 'ArrayList', clientRecords: List['Client'], ):
    """
    Tests the time taken to add, display, and remove Client records from an ArrayList.

    This function simulates a credit card call center scenario where representatives need to:
    1. Add client records to the ArrayList.
    2. Display 1000 random client records.
    3. Remove 1000 random client records.

    The function measures the time taken to complete these operations and logs the total elapsed time. 
    The recorded time can be used for performance analysis in the "Add, display, and remove records" 
    scenario for an Excel table or report.

    Args:
        numofClients (int): The number of Client objects to be added, displayed, and removed from the ArrayList.
        arrayList (ArrayList): An instance of the ArrayList class representing the data structure 
                               in which client records will be added, displayed, and removed.
        clientRecords (list of Client): A list containing Client objects to be added to the ArrayList.

    Returns:
        None
    """
    startTime = time.time()
    # append to array.
    appendToArray(numofClients, arrayList, clientRecords)

    # Display 1000 random records.
    for i in range(1000):
        smallest_id = 100001
        largest_id = smallest_id + numofClients
        random_num = random.randint(smallest_id, largest_id)
        #print(funWithArrays.search(Client(random_num)))
        print(arrayList.search_sorted(Client(random_num)))
    
    # Delete 1000 random records
    for i in range(1000):
        smallestId = 100001
        largestId = smallestId + numofClients
        random_num = random.randint(smallest_id, largest_id)
       #print(funWithArrays.search(Client(random_num))) #FIXME allow user to choose.
        print(arrayList.search_sorted(Client(random_num)))

    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f"\n3.\tTime taken to add {numofClients}, and then display and remove 1000 random client records: {elapsedTime:.6f} seconds")
    
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

def createClientRecords():
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
    clientRecords = createClientRecords()
    Quicksort.sort(clientRecords) #FIXME make this an optional call for user.
    newArray = ArrayList()
    numofClients = len(clientRecords)
    return newArray, numofClients, clientRecords

def checkForExistingArray(existingArray = None):
    if not existingArray:
        logging.error("The array is empty or not provided. Create an in the menu.")
        return False
    else:
        logging.debug("Using pre-existing array data!")
        return True


def main():
    """clientRecords = []
    numofClients = createClientRecords(clientRecords)
    Quicksort.sort(clientRecords) #FIXME make this an optional call for user.
    funWithArrays = ArrayList()
    numofClients = len(clientRecords)"""
    checkForExistingArray()
    funWithArrays, numofClients, clientRecords = createClientRecords()
    #print(numofClients) #FIXME make this into a test? 
    testNumberOne(numofClients, funWithArrays, clientRecords)
    testNumberOneContinued(numofClients, funWithArrays, clientRecords) # deletes funwitharray data
    appendToArray(numofClients, funWithArrays, clientRecords)
    testNumberTwo(numofClients, funWithArrays, clientRecords)
    testNumberThree(numofClients, funWithArrays, clientRecords)


if __name__ == "__main__":
    main()


