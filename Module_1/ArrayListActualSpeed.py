#Name: Christopher Barfield
#Date:  11/2/2024

# local
from Client import Client
from utilities import (
    appendToArray
)

# built-in
from datetime import date
import time
import random


def testNumberOne(numofClients, clientRecords):
    """
    Test Scenario 1: Adding records to the end of the ArrayList.

    This function tests how long it takes to add `numofClients` client records 
    to the ArrayList. The records are appended sequentially to the data structure.

    Args:
        numofClients (int): The number of client records to add.
        clientRecords (list): A list containing Client objects to be added.

    Returns:
        ArrayList: An ArrayList containing the added client records.

    Prints:
        Execution time to add the records.
    """
    startTime = time.time()
    arrayList = appendToArray(numofClients, clientRecords)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f"\n1.\tTime taken to add {numofClients} client records to ArrayList: {elapsedTime:.6f} seconds")

    return arrayList


def testNumberOneContinued(numofClients, arrayList):
    """
    Test Scenario 1-2: Removing records from the front of the ArrayList.

    This function tests how long it takes to remove `numofClients` client records 
    from the front of the ArrayList, one record at a time.

    Args:
        numofClients (int): The number of client records to remove.
        arrayList (ArrayList): The ArrayList from which records will be removed.

    Prints:
        Execution time to remove the records.
    """
    startTime = time.time()
    for i in range(numofClients):
        arrayList.remove_at(0)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f"\n1-2.\tTime taken to remove {numofClients} client records from ArrayList: {elapsedTime:.6f} seconds")


def testNumberTwo(numofClients, arrayList):
    """
    Test Scenario 2: Displaying random records from the ArrayList.

    This function tests how long it takes to retrieve 1000 random client records 
    from the ArrayList. Records are searched using random indices.

    Args:
        numofClients (int): The total number of client records in the ArrayList.
        arrayList (ArrayList): The ArrayList containing the client records.

    Returns:
        ArrayList: The original ArrayList after testing.

    Prints:
        Execution time to retrieve random records.
    """
    startTime = time.time()
    for i in range(1000):
        smallest_id = 100001
        largest_id = smallest_id + numofClients
        random_num = random.randint(smallest_id, largest_id)
        print(arrayList.search_sorted(Client(random_num)))
    
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f"\n2.\tTime taken to search for {numofClients} random client records: {elapsedTime:.6f} seconds")
    return arrayList


def testNumberThree(numofClients, clientRecords):
    """
    Test Scenario 3: Adding, displaying, and removing records from the ArrayList.

    This function tests a full workflow: adding client records, displaying random 
    records, and removing random records from the ArrayList. This simulates a 
    credit card call center scenario where records are frequently added, queried, 
    and removed.

    Args:
        numofClients (int): The number of client records to process.
        clientRecords (list): A list containing Client objects to be added.

    Returns:
        ArrayList: The final ArrayList after all operations are performed.

    Prints:
        Execution time to complete the add, display, and remove operations.
    """
    startTime = time.time()
    
    # Step 1: Add records to the ArrayList
    arrayList = appendToArray(numofClients, clientRecords)

    # Step 2: Display 1000 random records
    for i in range(1000):
        smallest_id = 100001
        largest_id = smallest_id + numofClients
        random_num = random.randint(smallest_id, largest_id)
        print(arrayList.search_sorted(Client(random_num)))

    # Step 3: Delete 1000 random records
    for i in range(1000):
        smallest_id = 100001
        largest_id = smallest_id + numofClients
        random_num = random.randint(smallest_id, largest_id)
        print(arrayList.search_sorted(Client(random_num)))

    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f"\n3.\tTime taken to add, display, and remove 1000 random client records: {elapsedTime:.6f} seconds")
    return arrayList
