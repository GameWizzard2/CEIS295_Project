#Name: Christopher Barfield
#Date:  11/2/2024


#Local
from .ArrayList import ArrayList
from .Utilities import ( 
    appendToArray, 
    remove_from_array, 
    create_client_records, 
    checkForExistingArray
)

from Client import Client
from SortingAlgo.Quicksort import Quicksort

# Imported
from typing import List

# BuiltIn
import time
import random



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
        elaspedTime from test
    """
    startTime = time.time()
    appendToArray(numofClients, arrayList, clientRecords)
    endTime = time.time()
    return endTime - startTime

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
        elaspedTime from test

    """
    startTime = time.time()
    remove_from_array(numofClients, arrayList)
    endTime = time.time()
    return endTime - startTime

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
        elaspedTime from test
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
    return endTime - startTime

def testNumberThree(numofClients: int, arrayList: 'ArrayList' = None, clientRecords: List['Client'] = None, ):
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
        elaspedTime from test
    """
    startTime = time.time()
    # append to array.
    appendToArray(numofClients, arrayList, clientRecords)

    # Display 1000 random records.
    for i in range(1000):
        smallest_id = 100001
        largest_id = smallest_id + numofClients
        random_num = random.randint(smallest_id, largest_id)
        print(arrayList.search(Client(random_num)))
        #print(arrayList.search_sorted(Client(random_num)))

    # Delete 1000 random records
    remove_from_array(numofClients, arrayList)


    endTime = time.time()
    return endTime - startTime



def main():
    """clientRecords = []
    numofClients = create_client_records(clientRecords)
    Quicksort.sort(clientRecords) #FIXME make this an optional call for user.
    funWithArrays = ArrayList()
    numofClients = len(clientRecords)"""
    checkForExistingArray()
    funWithArrays, numofClients, clientRecords = create_client_records()
    #print(numofClients) #FIXME make this into a test? 
    testNumberOne(numofClients, funWithArrays, clientRecords)
    testNumberOneContinued(numofClients, funWithArrays, clientRecords) # deletes funwitharray data
    appendToArray(numofClients, funWithArrays, clientRecords)
    testNumberTwo(numofClients, funWithArrays, clientRecords)
    testNumberThree(numofClients, funWithArrays, clientRecords)


if __name__ == "__main__":
    main()


