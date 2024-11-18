from Array import (createClientRecords,
                   createArray,
                   checkForExistingArray,
                   appendToArray,
                   ArrayList, 
                   testNumberOne, 
                   testNumberOneContinued,
                   testNumberTwo,
                   testNumberThree,
                   )
from GUI import ProjectApp
from Logger import CustomLogger
from SortingAlgo import Quicksort
from datetime import date
import sys


def main():
    # Setup logger.
    CustomLogger.main()
    # display name and date in output
    print("Name:", "Christopher H Barfield")
    print("Date:", date.today())

    clientRecords = []
    createClientRecords(clientRecords)
    Quicksort.sort(clientRecords) #FIXME make this an optional call for user.
    funWithArrays = ArrayList()
    numofClients = len(clientRecords)
    #print(numofClients) #FIXME make this into a test? 
    testNumberOne(numofClients, funWithArrays, clientRecords)
    testNumberOneContinued(numofClients, funWithArrays, clientRecords) # deletes funwitharray data
    appendToArray(numofClients, funWithArrays, clientRecords)
    testNumberTwo(numofClients, funWithArrays, clientRecords)
    testNumberThree(numofClients, funWithArrays, clientRecords)

"class MyWidget(QtWidgets.QWidget):"


if __name__ == "__main__":
    #
    CustomLogger.main()
    ProjectApp().run()