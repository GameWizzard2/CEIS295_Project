from pydoc import cli
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
from PySide6.QtCore import Slot
import sys
import logging
import time

# Local Imports
from Array import (create_client_records,
                   createArray,
                   checkForExistingArray,
                   appendToArray,
                   ArrayList, 
                   testNumberOne, 
                   testNumberOneContinued,
                   testNumberTwo,
                   testNumberThree,
                   )
from GUI.Helpers.Helpers_GUI import show_message_box
from GUI.Helpers.Array_Model import ArrayModel


#FIXME logging is not displaying to terminal
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
        self.array_test_one_button = QPushButton("Array List: Test One part A")
        self.array_test_one_part_two_button = QPushButton("Array List: Test One part B")
        self.array_test_two_button = QPushButton("Array List: Test Two")
        self.array_test_three_button = QPushButton("Array List: Test Three")
        self.createArrayButton = QPushButton("Create Array")

        # Initialize array model
        self.model = ArrayModel()

    def window_layout(self):
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
        self.window_layout()
        self.button_functions()
        self.show_buttons_in_layout()
        # Run the main Qt loop
        self.app.exec()

    def button_functions(self):
        """
        Connects button clicks to their corresponding functions.
        """
        self.array_test_one_button.clicked.connect(self.array_test_one_a)
        self.array_test_one_part_two_button.clicked.connect(self.array_test_one_b)
        self.array_test_two_button.clicked.connect(self.array_test_two)
        self.array_test_three_button.clicked.connect(self.array_test_three)
        self.createArrayButton.clicked.connect(self.create_array_fuction)
        #TODO add remove array button

    def show_buttons_in_layout(self):
        """
        Adds buttons to the window layout and ensures they are visible.
        """
        self.layout.addWidget(self.array_test_one_button)
        self.layout.addWidget(self.array_test_one_part_two_button)
        self.layout.addWidget(self.array_test_two_button)
        self.layout.addWidget(self.array_test_three_button)
        self.layout.addWidget(self.createArrayButton)
        self.array_test_one_button.show()
        self.array_test_one_part_two_button.show()
        self.array_test_two_button.show()
        self.array_test_three_button.show()
        self.createArrayButton.show()
        logging.debug("buttons added to window layout from show_buttons_in_layout")

    def check_for_array(self):
        if not checkForExistingArray(self._client_count, self._array_list):
            message = ("Please click the create array button before running this test")
            show_message_box("Error: No existing array.", message)
            # Exit the function early if check fails
            return False
        else:
            return True
    # Getter and Setter for array_list
    @property
    def array_list(self):
        """Getter for the array list."""
        return self._array_list

    @array_list.setter
    def array_list(self, value):
        """Setter for the array list."""
        if not isinstance(value, ArrayList):
            raise ValueError("array_list must be an instance of ArrayList")
        self._array_list = value

    # Getter and Setter for client_count
    @property
    def client_count(self):
        """Getter for the client count."""
        return self._client_count

    @client_count.setter
    def client_count(self, value):
        """Setter for the client count."""
        if not isinstance(value, int) or value < 0:
            raise ValueError("client_count must be a non-negative integer")
        self._client_count = value

    # Getter and Setter for client_data_records
    @property
    def client_data_records(self):
        """Getter for the client data records."""
        return self._client_data_records

    @client_data_records.setter
    def client_data_records(self, value):
        """Setter for the client data records."""
        if not isinstance(value, list):
            raise ValueError("client_data_records must be a list")
        self._client_data_records = value


    @Slot()
    def create_array_fuction(self):#FIXME Not working as intended for test 2, it displays none make this fuction create an array then add the button above
        """
        Creates an array and runs a test on it.

        This function initializes a new array, checks if an existing array
        exists, and then runs Test Number One.
        """
        self._array_list, self._client_count, self._client_data_records = createArray()
        self._client_count, self._array_list, self._client_data_records = self.model.create_array(
            self._client_count, 
            self._array_list, 
            self._client_data_records
            )
        logging.info("\nCreating Array!\nArray Created successfully!")

    @Slot()
    def sort_array(self):#FIXME make this fuction create an array then add the button above
        print("work on implementing fuction using the quicksort algo")

    @Slot()
    def array_test_one_a(self):
        """
        Runs Test Number One, Part A.

        This function checks for an existing array and creates a new one
        if necessary, then runs Test Number One.
        """
        logging.debug("Running Test One, Creating Array!")
        funWithArrays, numofClients, clientRecords = createArray()
        self._array_list = funWithArrays
        self._client_count = numofClients
        self._client_data_records = clientRecords
        elapsedTime = testNumberOne(numofClients, funWithArrays, clientRecords)

        message= (
                f"Clients have been successfully added!\n\nTerminal Output:"
                f"\nTime taken to add {self._client_count} client records:\n"
                f"{elapsedTime:.6f} seconds"
                )
        show_message_box("Action Completed", message)

#FIXME Make sure it informs user when an array has not been created to delete Logging needs to be displayed.
    @Slot()
    def array_test_one_b(self):
        if self.check_for_array() is False:
            return False
        
        else:
            # Proceed if checkForExistingArray returned True
            elapsedTime = testNumberOneContinued(self._client_count, self._array_list)
            message= (
                    f"Clients have been successfully removed!\n\nOutput:"
                    f"\nTime taken to delete {self._client_count} client records:\n"
                    f"{elapsedTime:.6f} seconds"
                    )
            logging.info("All clients have been removed!")
            self._client_count = 0
            show_message_box("Action Completed", message)

#FIXME Make sure it informs user when an array has not been created to delete.
    @Slot()
    def array_test_two(self):
        
        if self.check_for_array() is False:
            return False
        
        else:
            # Proceed if checkForExistingArray returned True
            logging.info("Running Test Two!")
            elapsedTime = testNumberTwo(self._client_count, self._array_list)
            logging.info("1000 random records have been displayed")
            message = (f"\n2.\tTime taken to search for {self._client_count} random client records:\n"
                    F"{elapsedTime:.6f} seconds")
            show_message_box("Action Completed", message)


    #FIXME launch add records then all the other test
    @Slot()
    def array_test_three(self):
        
        # Proceed if checkForExistingArray returned True
        logging.info("Running Test Three!")

        # Add records
        funWithArrays, numofClients, clientRecords = createArray()
        self._array_list = funWithArrays
        self._client_count = numofClients
        self._client_data_records = clientRecords

        # Call older test and add up time
        elapsedTime = testNumberOne(self._client_count, self._array_list, self._client_data_records)
        elapsedTime =+ testNumberTwo(self._client_count, self._array_list)
        elapsedTime =+ testNumberOneContinued(self._client_count, self._array_list)

        message = (f"\n3.\tTime taken to add {self._client_count}, display, then remove 1000 random "
                   f"client records:\n{elapsedTime:.6f} seconds")
        show_message_box("Action Completed", message)

        # Set Client records to zero after test
        self._client_count = 0
        self._client_data_records = None
        