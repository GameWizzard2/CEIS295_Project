#Name: Christopher Barfield
#Date:  11/26/2024

from LinearSearch import LinearSearch
from BinarySearch import BinarySearch
from Quicksort import Quicksort
from Client import Client

from datetime import date
import random
import time
import os

def begin_linear_search_test(numofClients, clientRecords):

    startTime = time.time()
    startRecord = 100001
    endRecord = startRecord + numofClients
    # search for 1000 random records
    for i in range(1000):
        clientID = random.randint(startRecord,endRecord)
        clt = Client(clientID)
        result = LinearSearch.search(clientRecords,clt)
        if result is None:
            print(f"{clt}: was not found.")
        else:
            print(result)
            endTime = time.time()
            elapsedTime = endTime - startTime
    print(f"The total time to search 1000 records using the linear search algorithm with {numofClients} records was {elapsedTime:.6f}")

def begin_binary_search_test(numofClients, clientRecords):

    startTime = time.time()
    startRecord = 100001
    endRecord = startRecord + numofClients
    # search for 1000 random records
    for i in range(1000):
        clientID = random.randint(startRecord,endRecord)
        clt = Client(clientID)
        result = BinarySearch.search(clientRecords,clt)
        if result is None:
            print(f"{clt}: was not found.")
        else:
            print(result)
            endTime = time.time()
            elapsedTime = endTime - startTime
    print(f"The total time to search 1000 records using the Binary search algorithm with {numofClients} records was {elapsedTime:.6f}")

def search_test_options():
    """
    Prompt the user to select a search test to run on the client records.

    This function allows the user to choose between a linear search test or a binary search test.
    The corresponding test function is returned for execution.

    Returns:
        tuple: A tuple containing the name of the search test (str) and the function to execute (callable).

    Prints:
        A list of search test options for the user to choose from.

    Raises:
        ValueError: If the user inputs a non-integer value.
    """
    searchOptions = {
        1: ('Linear Search Test', begin_linear_search_test),
        2: ('Binary Search Test', begin_binary_search_test)
    }

    print("Select the search test to perform:")
    for key, (DisplayName, searchFunction) in searchOptions.items():
        print(f"{key}: {DisplayName}")

    searchChoice = int(input("Enter the number corresponding to your choice: "))
    searchName, searchFunction = searchOptions.get(searchChoice, (None, None))

    if not searchFunction:
        print("Invalid search test choice. Please run the program again and select a valid option.\nClosing program...")
        return None, None

    print(f"\nSearch test chosen: {searchName}... Running...\n")
    return searchName, searchFunction