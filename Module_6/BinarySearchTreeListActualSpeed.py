#Name: Christopher Barfield
#Date:  11/26/2024

# local
from Client import Client
from utilities import (
    remove_records_from_front,
    add_records,
    display_one_thousand_random_records,
    remove_one_thousand_random_records
)

# built-in
from datetime import date
import time

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
