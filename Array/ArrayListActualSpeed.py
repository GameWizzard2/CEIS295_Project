#Name: Christopher Barfield
#Date:  11/2/2024

from Array.ArrayList import ArrayList #FIXME Find out if you can put this in __init__.py in the folder Array??? Otherwise it has to be called like this?
from Client import Client
from SortingAlgo.Quicksort import Quicksort
from datetime import date
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

    Returns:
        None
    """
    startTime = time.time()
    appendToArray(numofClients, arrayList, clientRecords)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f"\n1.\tTime taken to add {numofClients} client records to ArrayList: {elapsedTime:.6f} seconds")

# Consider this removeFromStart()
def testNumberOneContinued():
    """
    11.	Continue the ArrayListActualSpeed code and write code to test how much time it takes to remove 
    all of the Client objects from the front of the ArrayList, one object at a time. Add this time to 
    the spreadsheet into the “Pull all records off front of data structure” row in the Excel table.
    """
    startTime = time.time()
    for i in range(numofClients):
        funWithArrays.remove_at(0)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f"\n1-2.\tTime taken to remove {numofClients} client records from ArrayList: {elapsedTime:.6f} seconds")

# Consider this displayAThousandRandomRecords()
def testNumberTwo(numOfClients):
    """
    12.	Now, let’s test the second scenario. A customer service center receives calls from random customers. 
    The customer service center must be able to quickly pull up the customer’s record. Is the ArrayList good 
    for this scenario? Let’s see how long it takes to pull up random records. Write code to add all of the 
    customers to the ArrayList again since we deleted all of the customers on the last step.  Now, write code 
    to test how much time it takes to display many random records. Add this time to the spreadsheet into the 
    “Display random records” row in the Excel table.
    """
    # How long does it take to display 1000 random records?
    startTime = time.time()
    for i in range(1000):
        smallest_id = 100001
        largest_id = smallest_id + numofClients
        random_num = random.randint(smallest_id, largest_id)
        #print(funWithArrays.search(Client(random_num)))
        print(funWithArrays.search_sorted(Client(random_num)))


    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f"\n2.\tTime taken to search for {numOfClients} random client records: {elapsedTime:.6f} seconds")

def testNumberThree(numOfClients):
    """
    3.	Let’s consider the third scenario. Consider a credit card call center. The representatives may sign up new 
    credit card accounts (add records). The representatives may answer customers’ questions (display random records). 
    Finally, the representatives may delete a paid-off account at the request of the customer (remove records). Write 
    code to test how much time it takes to add the Client records to the ArrayList, then randomly display records, 
    and then randomly delete records. Add this time to the spreadsheet into the bottom row.
    """
    startTime = time.time()
    # append to array.
    appendToArray(numofClients)

    # Display 1000 random records.
    for i in range(1000):
        smallest_id = 100001
        largest_id = smallest_id + numofClients
        random_num = random.randint(smallest_id, largest_id)
        #print(funWithArrays.search(Client(random_num)))
        print(funWithArrays.search_sorted(Client(random_num)))
    
    # Delete 1000 random records
    for i in range(1000):
        smallestId = 100001
        largestId = smallestId + numofClients
        random_num = random.randint(smallest_id, largest_id)
       #print(funWithArrays.search(Client(random_num)))
        print(funWithArrays.search_sorted(Client(random_num)))

    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f"\n3.\tTime taken to add {numofClients}, and then display and remove 1000 random client records: {elapsedTime:.6f} seconds")
    



def appendToArray(numofClients, arrayList, clientRecords):
    """
    Append clientRecords to an array object
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


