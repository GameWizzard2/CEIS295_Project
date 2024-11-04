from Array import (createClientRecords, 
                   appendToArray,
                   ArrayList, 
                   testNumberOne, 
                   testNumberOneContinued,
                   testNumberTwo,
                   testNumberThree,
                   )
from SortingAlgo import Quicksort
from datetime import date


# display name and date in output
print("Name:", "Christopher H Barfield")
print("Date:", date.today())

clientRecords = []


createClientRecords(clientRecords)
Quicksort.sort(clientRecords) #FIXME make this an optinal call for user.
funWithArrays = ArrayList()
numofClients = len(clientRecords)
#print(numofClients) #FIXME make this into a test? 
testNumberOne(numofClients, funWithArrays, clientRecords)
testNumberOneContinued(numofClients, funWithArrays, clientRecords) # deletes funwitharray data
appendToArray(numofClients, funWithArrays, clientRecords)
testNumberTwo(numofClients, funWithArrays, clientRecords)
testNumberThree(numofClients, funWithArrays, clientRecords)