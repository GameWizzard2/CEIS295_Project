#Name: Christopher Barfield
#Date:  11/2/2024

from Array.ArrayList import ArrayList #FIXME Find out if you can put this in __init__.py in the folder Array??? Otherwise it has to be called like this?
from Client import Client
from SortingAlgo.Quicksort import Quicksort
from datetime import date
from typing import List
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
def testNumberOneContinued(numofClients: int, arrayList: 'ArrayList', clientRecords: List['Client']):
    """
    Tests the time taken to remove Client objects from the front of an ArrayList, one at a time.

    This function measures the performance of removing Client objects from the front of an 
    ArrayList instance, simulating the process of pulling records one by one. The time taken 
    for the operation is recorded and can be used for performance analysis in the 
    "Pull all records off front of data structure" scenario for an Excel table or report.

    Args:
        numofClients (int): The number of Client objects to be added to the ArrayList.
        arrayList (ArrayList): An instance of the ArrayList class representing the data structure 
                           to which Client objects will be added.
        clientRecords (list): A list containing Client objects to be added to the ArrayList.

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
def testNumberTwo(numofClients: int, arrayList: 'ArrayList', clientRecords: List['Client']):
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
        clientRecords (list of Client): A list containing Client objects.

    Returns:
        None
    """
    # How long does it take to display 1000 random records?
    startTime = time.time()
    for i in range(1000):
        smallest_id = 100001
        largest_id = smallest_id + numofClients
        random_num = random.randint(smallest_id, largest_id)
        #print(funWithArrays.search(Client(random_num))) #FIXME allow user to choose.
        print(arrayList.search_sorted(Client(random_num)))


    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f"\n2.\tTime taken to search for {numofClients} random client records: {elapsedTime:.6f} seconds")

def testNumberThree(numofClients: int, arrayList: 'ArrayList', clientRecords: List['Client'], ):
    """
    3.	Let’s consider the third scenario. Consider a credit card call center. The representatives may sign up new 
    credit card accounts (add records). The representatives may answer customers’ questions (display random records). 
    Finally, the representatives may delete a paid-off account at the request of the customer (remove records). Write 
    code to test how much time it takes to add the Client records to the ArrayList, then randomly display records, 
    and then randomly delete records. Add this time to the spreadsheet into the bottom row.
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

def createClientRecords(clientRecords):
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
        

def main():
    # display name and date in output
    print("Name:", "Christopher H Barfield")
    print("Date:", date.today())

    clientRecords = []
    createClientRecords()
    Quicksort.sort(clientRecords)
    funWithArrays = ArrayList()
    numofClients = len(clientRecords)
    testNumberOne()
    testNumberOneContinued() # deletes funwitharray data
    appendToArray(numofClients)
    testNumberTwo(numofClients)
    testNumberThree(numofClients)

if __name__ == "__main__":
    main()


