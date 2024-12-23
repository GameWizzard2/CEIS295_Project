# Local
from array import array
from ArrayListActualSpeed import (
    testNumberOne,
    testNumberOneContinued,
    testNumberTwo,
    testNumberThree
)
from utilities import (
    appendToArray,
    userContinueInput,
    createClientRecords
)
from Quicksort import Quicksort
from ArrayList import ArrayList

# Built-in
from datetime import date


def main():
    # display name and date in output
    print("Name:", "Christopher H Barfield")
    print("Date:", date.today())

    clientRecords = []
    clientRecords = createClientRecords(clientRecords)
    Quicksort.sort(clientRecords)
    numofClients = len(clientRecords)

    arrayList = testNumberOne(numofClients, clientRecords)
    arrayList = testNumberOneContinued(numofClients, arrayList) # deletes funwitharray data
    userContinueInput()
    arrayList = appendToArray(numofClients, clientRecords)
    arrayList = testNumberTwo(numofClients, arrayList)
    userContinueInput()
    arrayList = testNumberThree(numofClients, clientRecords)
    userContinueInput()


if __name__ == '__main__':
    main()