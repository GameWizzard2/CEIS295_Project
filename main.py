from Array import createClientRecords, ArrayList, testNumberOne
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
#testNumberOneContinued() # deletes funwitharray data
#appendToArray(numofClients)
#testNumberTwo(numofClients)
#testNumberThree(numofClients)