#Name: Christopher Barfield
#Date:  11/2/2024

from ArrayList import ArrayList
from Client import Client
from Quicksort import Quicksort
from datetime import date
import time
import random
import sys


# Consdier this addRecords()
def testNumberOne():
    """
    Let’s test the first scenario. If you accept jobs at the back of the line and then process the jobs 
    from the front of the line, which data structure is best? Write code to test how much time that 
    it takes to add the Client objects from the list into the ArrayList data structure. 
    The ArrayList automatically adds the new records to the end of the data structure so add this 
    time to the spreadsheet into the “Add many records to end of data structure” row in the Excel table.
    """
    startTime = time.time()
    appendToArray(numofClients)
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
    
def appendToArray(numOfClients):
    """
    Append clientRecords to an array object
    """
    for i in range(numofClients):
        funWithArrays.append(clientRecords[i])

def createClientRecords():
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

def userContinueInput():
    print("Press \"Enter\" to continue...")
    sys.stdin.read(1)  # Reads one character (like Enter) from standard input

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
userContinueInput()
appendToArray(numofClients)
testNumberTwo(numofClients)
userContinueInput()
testNumberThree(numofClients)
userContinueInput()

