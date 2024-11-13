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
from Logger import CustomLogger
from SortingAlgo import Quicksort
from datetime import date
import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
from PySide6.QtCore import Slot

class ProjectApp():
    def __init__(self):
        # Create the Qt Application
        self.app = QApplication(sys.argv)

        # Create a main window to hold widgets.
        self.window = QWidget()
        self.layout = QVBoxLayout()

        # Create a button, connect it and show it
        self.button = QPushButton("Array List: Test One part A")
        self.button2 = QPushButton("Array List: Test One part A")
        self.button3 = QPushButton("Array List: Test Two")
        self.button4 = QPushButton("Array List: Test Three part A")
        self.button5 = QPushButton("Add Array")

    def windowLayout(self):
        # Set the layout for the window and show it
        self.window.setLayout(self.layout)
        self.window.setWindowTitle("Project App")
        self.window.show()

    def run(self):
        self.windowLayout()
        self.connectRunButton()
        self.showButtonsInLayout()
        # Run the main Qt loop
        self.app.exec()

    def connectRunButton(self):
        # connect the buttons to a fuction.
        self.button.clicked.connect(self.arrayTestOneA)
        self.button2.clicked.connect(self.arrayTestOneA)
        self.button3.clicked.connect(self.arrayTestOneA)
        self.button4.clicked.connect(self.arrayTestOneA)
        self.button5.clicked.connect(self.arrayTestOneA)

    def showButtonsInLayout(self):
        # Show the buttons in the main window.
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.layout.addWidget(self.button4)
        self.layout.addWidget(self.button5)
        self.button.show()
        self.button2.show()
        self.button3.show()
        self.button4.show()
        self.button5.show()
        CustomLogger.debug("buttons added to window layout from showButtonsInLayout")


    @Slot()
    def arrayTestOneA(self):#TODO make more button fuctions
        print("Running Test One!")
        checkForExistingArray() #TODO make this its own button.
        funWithArrays, numofClients, clientRecords = createArray()
        testNumberOne(numofClients, funWithArrays, clientRecords)

    @Slot()
    def arrayTestOneB(self):#TODO make more button fuctions
        print("Running Test One!")
        checkForExistingArray() #TODO make this its own button.
        funWithArrays, numofClients, clientRecords = createArray()
        testNumberOne(numofClients, funWithArrays, clientRecords)

    @Slot()
    def arrayTestTwo(self):#TODO make more button fuctions
        print("Running Test One!")
        checkForExistingArray() #TODO make this its own button.
        funWithArrays, numofClients, clientRecords = createArray()
        testNumberOne(numofClients, funWithArrays, clientRecords)

    @Slot()
    def arrayTestThree(self):#TODO make more button fuctions
        print("Running Test One!")
        checkForExistingArray() #TODO make this its own button.
        funWithArrays, numofClients, clientRecords = createArray()
        testNumberOne(numofClients, funWithArrays, clientRecords)

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
    ProjectApp().run()