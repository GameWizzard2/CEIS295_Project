#Name: Christopher Barfield
#Date:  11/2/2024

# local
from Client import Client
from utilities import (
    appendToArray,
    createClientRecords,
    userContinueInput
)

# built-in
from datetime import date
import time
import random


# Consdier this addRecords()
def testNumberOne(numofClients, clientRecords):
    """
    Let’s test the first scenario. If you accept jobs at the back of the line and then process the jobs 
    from the front of the line, which data structure is best? Write code to test how much time that 
    it takes to add the Client objects from the list into the ArrayList data structure. 
    The ArrayList automatically adds the new records to the end of the data structure so add this 
    time to the spreadsheet into the “Add many records to end of data structure” row in the Excel table.
    """
    startTime = time.time()
    arrayList = appendToArray(numofClients, clientRecords)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f"\n1.\tTime taken to add {numofClients} client records to ArrayList: {elapsedTime:.6f} seconds")

    return arrayList
# Consider this removeFromStart()
def testNumberOneContinued(numofClients, arrayList):
    """
    11.	Continue the ArrayListActualSpeed code and write code to test how much time it takes to remove 
    all of the Client objects from the front of the ArrayList, one object at a time. Add this time to 
    the spreadsheet into the “Pull all records off front of data structure” row in the Excel table.
    """
    startTime = time.time()
    for i in range(numofClients):
        arrayList.remove_at(0)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f"\n1-2.\tTime taken to remove {numofClients} client records from ArrayList: {elapsedTime:.6f} seconds")

# Consider this displayAThousandRandomRecords()
def testNumberTwo(numofClients, arrayList):
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
        print(arrayList.search_sorted(Client(random_num)))


    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f"\n2.\tTime taken to search for {numofClients} random client records: {elapsedTime:.6f} seconds")
    return arrayList

def testNumberThree(numofClients, clientRecords):
    """
    3.	Let’s consider the third scenario. Consider a credit card call center. The representatives may sign up new 
    credit card accounts (add records). The representatives may answer customers’ questions (display random records). 
    Finally, the representatives may delete a paid-off account at the request of the customer (remove records). Write 
    code to test how much time it takes to add the Client records to the ArrayList, then randomly display records, 
    and then randomly delete records. Add this time to the spreadsheet into the bottom row.
    """
    startTime = time.time()
    # append to array.
    arrayList = appendToArray(numofClients, clientRecords)

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
       #print(arrayList.search(Client(random_num)))
        print(arrayList.search_sorted(Client(random_num)))

    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f"\n3.\tTime taken to add {numofClients}, and then display and remove 1000 random client records: {elapsedTime:.6f} seconds")
    return arrayList