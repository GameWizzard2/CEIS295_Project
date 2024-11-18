from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
from PySide6.QtCore import Slot
import sys
import logging
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

class ProjectApp():
    """
    A GUI application for interacting with array operations using PySide6.

    This class creates a PySide6-based GUI with buttons to trigger 
    different operations related to arrays and their tests.
    """
    def __init__(self):
        """
        Initializes the GUI application and its components.

        Creates an instance of the QApplication, sets up the main window,
        layout, and initializes buttons for array operations.
        """
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
        """
        Sets up the layout for the main window and displays it.
        """
        self.window.setLayout(self.layout)
        self.window.setWindowTitle("Project App")
        self.window.show()

    def run(self):
        """
        Runs the GUI application.

        This method sets up the window layout, connects button actions,
        adds buttons to the layout, and starts the main event loop.
        """
        self.windowLayout()
        self.connectRunButton()
        self.showButtonsInLayout()
        # Run the main Qt loop
        self.app.exec()

    def connectRunButton(self):
        """
        Connects button clicks to their corresponding functions.
        """
        self.button.clicked.connect(self.arrayTestOneA)
        self.button2.clicked.connect(self.arrayTestOneA)
        self.button3.clicked.connect(self.arrayTestOneA)
        self.button4.clicked.connect(self.arrayTestOneA)
        self.button5.clicked.connect(self.arrayTestOneA)

    def showButtonsInLayout(self):
        """
        Adds buttons to the window layout and ensures they are visible.
        """
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
        logging.debug("buttons added to window layout from showButtonsInLayout")

    @Slot()
    def create_array(self):#FIXME make this fuction create an array then add the button above
        """
        Creates an array and runs a test on it.

        This function initializes a new array, checks if an existing array
        exists, and then runs Test Number One.
        """
        print("Adding Array!")
        checkForExistingArray() #TODO make this its own button.
        funWithArrays, numofClients, clientRecords = createArray()
        testNumberOne(numofClients, funWithArrays, clientRecords)

    @Slot()
    def arrayTestOneA(self, ):#TODO make more button fuctions
        """
        Runs Test Number One, Part A.

        This function checks for an existing array and creates a new one
        if necessary, then runs Test Number One.
        """
        print("Running Test One!")
        checkForExistingArray() #TODO make this its own button.
        funWithArrays, numofClients, clientRecords = createArray()
        testNumberOne(numofClients, funWithArrays, clientRecords)

    @Slot()
    def arrayTestOneB(self, numofClients: int, arrayList: 'ArrayList'):#FIXME must call an existing array.
        logging.info("Running Test One Part B!")
        checkForExistingArray() #TODO make this its own button.
        
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
        