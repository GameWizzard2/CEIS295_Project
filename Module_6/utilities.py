# local
from Client import Client

# built-in
import sys
import random

def extractClientData(newList = []):
    input_file_name = '.\Module_6\ClientData.csv'
    with open(input_file_name) as infile:
        for line in infile:
            s = line.split(',')
            clientId = int(s[0])  # convert the default string to an int
            customerName = s[1]
            customerPhone = s[2]
            # Create a Call object based on the line from the file.
            callQueue = Client(clientId, customerName, customerPhone)
            # Add the call object to the list
            newList.append(callQueue)
        return newList

def add_records(numofRecords, clinetList, binaryTree):
    """
    binaryTree is a BinarySearchTree object
    """
    for i in range(numofRecords):
        binaryTree.insert(clinetList[i])
    return binaryTree

def display_one_thousand_random_records(numofClients, myBst):
    for i in range(1000):
        smallest_id = 100001
        largest_id = smallest_id + numofClients
        random_num = random.randint(smallest_id, largest_id)
        print(myBst.search(Client(random_num)))

def remove_one_thousand_random_records(numofClients, myBst):
    for i in range(1000):
        smallest_id = 100001
        largest_id = smallest_id + numofClients
        random_num = random.randint(smallest_id, largest_id)
        myBst.remove(Client(random_num))
    return myBst

def remove_records_from_front(numofRecords, binaryTree):
    for i in range(numofRecords):
        binaryTree.remove_minimum()

    return binaryTree

def userContinue():
    userInput = input("Continue (y/n)?")
    if userInput.lower() != "y":
        print("Exiting program")
        sys.exit()