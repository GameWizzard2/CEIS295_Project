# Local
from utilities import (
    extractClientData,
    add_records,
    userContinue
)
from BinarySearchTree import BinarySearchTree
from BinarySearchTreeListActualSpeed import (
    test_one,
    test_one_deletion,
    test_two,
    test_three
)

# built-in
import sys
from datetime import date

def main():
    print("Name:", "Christopher H Barfield")
    print(f"Date: {date.today()}\n")

    # Build the tree
    clientList = extractClientData()
    numofClients = len(clientList)
    myBst = BinarySearchTree()

    # Scenario one: Printer Queue/Call Queue/Service Queue
    print(f"Scenario: Printer Queue/Call Queue/Service Queue:\n{40 * '_'}")
    # Excecute Test one.
    myBst = test_one(numofClients, clientList, myBst)
    myBst = test_one_deletion(numofClients, myBst)

    userContinue()

    # clientsList need to be re-added to myBst before running the next test so that it works.
    myBst = add_records(numofClients, clientList, myBst)

    # Scenario Two: Customer Service Center
    print(f"Scenario: Customer Service Center, display 1000 random records:\n{40 * '_'}")
    test_two(numofClients, myBst)

    userContinue()

    # Scenario Three: Call Center
    print(f"Scenario: Add records, display records, remove random records:\n{40 * '_'}")
    test_three(numofClients, clientList, myBst)

if __name__ in "__main__":
    main()

