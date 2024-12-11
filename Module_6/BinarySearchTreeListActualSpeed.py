#Name: Christopher Barfield
#Date:  11/26/2024

from BinarySearchTree import BinarySearchTree
from Client import Client

from datetime import date
import sys
import random
import time

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
# Utitlities __________________________________________________
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


# Tests _________________________________________________
def test_one(numofRecords, clinetList, binaryTree):
    """
    binaryTree is a BinarySearchTree object
    """
    startTime = time.time()

    # Add records
    binaryTree = add_records(numofRecords, clinetList, binaryTree)

    endTime = time.time()
    elaspedTime = endTime - startTime
    print(f"Total time to add records: {elaspedTime:.6f}\n")
    return binaryTree

def test_one_deletion(numofRecords, binaryTree):
    startTime = time.time()

    #Remove records
    binaryTree = remove_records_from_front(numofRecords, binaryTree)
        
    endTime = time.time()
    elaspedTime = endTime - startTime
    print(f"Total time to remove records from the front: {elaspedTime:.6f}\n")
    return binaryTree

def test_two(numofClients, myBst):
    startTime = time.time()

    # display 1000 random records
    display_one_thousand_random_records(numofClients, myBst)

    endTime = time.time()
    elaspedTime = endTime - startTime
    print(f"Total time to display 1000 records: {elaspedTime:.6f}\n")


def test_three(numofRecords, clinetList, binaryTree):
    startTime = time.time()
    
    # Add more records instead of just records from the clientdata
    currentId = 100001 + numofRecords + 1
    for i in range(1000):
        binaryTree.insert(Client(currentId))
        currentId += 1

    # display 1000 random records
    display_one_thousand_random_records(numofRecords, binaryTree)


    #Remove records
    binaryTree = remove_one_thousand_random_records(numofRecords, binaryTree)


    endTime = time.time()
    elaspedTime = endTime - startTime
    print(f"Total time to add, display, and remove 1000 random records: {elaspedTime:.6f}\n")

def main():
    print("Name:", "Christopher H Barfield")
    print(f"Date: {date.today()}\n")

    clientList = extractClientData()
    numofClients = len(clientList)
    myBst = BinarySearchTree()

    # Scenario one: Printer Queue/Call Queue/Service Queue
    print(f"Scenario: Printer Queue/Call Queue/Service Queue:\n{40 * '_'}")
    # Excecute Test one.
    myBst = test_one(numofClients, clientList, myBst)
    myBst = test_one_deletion(numofClients, myBst)

    userInput = input("Continue (y/n)?")
    if userInput.lower() != "y":
        print("Exiting program")
        sys.exit()

    # clientsList need to be re-added to myBst before running the next test so that it works.
    myBst = add_records(numofClients, clientList, myBst)

    # Scenario Two: Customer Service Center
    print(f"Scenario: Customer Service Center, display 1000 random records:\n{40 * '_'}")
    test_two(numofClients, myBst)

    # Scenario Three: Call Center
    print(f"Scenario: Add records, display records, remove random records:\n{40 * '_'}")
    test_three(numofClients, clientList, myBst)

if __name__ in "__main__":
    main()

