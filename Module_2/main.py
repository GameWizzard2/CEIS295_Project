# Local
from array import array
from LinkedListActualSpeed import (
    testLinkedOne,
    testLinkedOneContinued,
    testLinkedTwo,
    testLinkedThree
)
from utilities import (
    appendToLinkedList,
    userContinueInput,
    createClientRecords
)
from LinkedList import LinkedList

# Built-in
from datetime import date


def main():
    # display name and date in output
    print("Name:", "Christopher H Barfield")
    print("Date:", date.today())
    clientRecords = createClientRecords()
    numofClients = len(clientRecords)
    linkedLists = LinkedList()

    testLinkedOne(numofClients, linkedLists, clientRecords)
    testLinkedOneContinued(numofClients, linkedLists)
    userContinueInput()
    appendToLinkedList(numofClients, linkedLists, clientRecords)
    testLinkedTwo(numofClients, linkedLists)
    userContinueInput()
    testLinkedThree(numofClients, linkedLists, clientRecords)
    userContinueInput()


if __name__ == '__main__':
    main()