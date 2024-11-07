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
import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot

class ProjectApp():
    def __init__(self):
        # Create the Qt Application
        self.app = QApplication(sys.argv)

        # Create a button, connect it and show it
        self.button = QPushButton("Click me")


    def run(self):
        self.connectRunButton()
        # Run the main Qt loop
        self.app.exec()
        

    def connectRunButton(self):
        self.button.clicked.connect(self.say_hello)
        self.button.show()


    @Slot()
    def say_hello(self):
        print("Button clicked, Hello!")
        testNumberOne(numofClients, funWithArrays, clientRecords)

def main():
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
    ProjectApp().run()