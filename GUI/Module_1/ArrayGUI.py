# Built-in
import sys
import logging

# Third Party
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
from PySide6.QtCore import Slot

# Local Imports
from Array import (createArray,
                   checkForExistingArray,
                   ArrayList, 
                   testNumberOne, 
                   testNumberOneContinued,
                   testNumberTwo,
                   Quicksort,
                   )
from GUI.Module_1 import show_message_box
from GUI.Module_1.Utilities.Array_Model import ArrayModel


class ArrayGUI(QWidget):
    """
    A GUI application for interacting with array operations using PySide6.

    This class creates a PySide6-based GUI with buttons to trigger 
    different operations related to arrays and their tests.
    """
    def __init__(self, parent=None):
        """
        Initializes the GUI application and its components.

        Creates an instance of the QApplication, sets up the main window,
        layout, and initializes buttons for array operations.
        """
        super().__init__(parent)

        #Initialize private attributes with default values.
        self._client_count = 0                # Initialize with a default integer
        self._client_data_records = []        # Initialize with an empty list
        self._array_list = None               # Initialize with None or a default ArrayList instance

        # Initialize array model
        self.model = ArrayModel()
        
        # Create a main window
        self.layout = QVBoxLayout(self)
        self.init_buttons()
        self.connect_signals()
        self.show_buttons_in_layout()
        self.setWindowTitle("Array Operations")

    def window_layout(self):
        """
        Sets up the layout for the main window and displays it.
        """
        self.window.setLayout(self.layout)
        self.window.setWindowTitle("Project App")
        self.window.show()

    def init_buttons(self):
        """Initialize all buttons."""
        self.array_test_one_button = QPushButton("Array List: Test One part A")
        self.array_test_one_part_two_button = QPushButton("Array List: Test One part B")
        self.array_test_two_button = QPushButton("Array List: Test Two")
        self.array_test_three_button = QPushButton("Array List: Test Three")
        self.createArrayButton = QPushButton("Create Array")
        self.removeArrayButton = QPushButton("Remove Array")
        self.sortArrayButton = QPushButton("Sort Array")

    def connect_signals(self):
        """
        Connects button clicks to their corresponding functions.
        """
        self.array_test_one_button.clicked.connect(self.array_test_one_a)
        self.array_test_one_part_two_button.clicked.connect(self.array_test_one_b)
        self.array_test_two_button.clicked.connect(self.array_test_two)
        self.array_test_three_button.clicked.connect(self.array_test_three)
        self.createArrayButton.clicked.connect(self.create_array_function)
        self.removeArrayButton.clicked.connect(self.remove_array)
        self.sortArrayButton.clicked.connect(self.sort_array)
        

    def show_buttons_in_layout(self):
        """
        Adds buttons to the window layout and ensures they are visible.
        """
        buttons = [
            self.array_test_one_button,
            self.array_test_one_part_two_button,
            self.array_test_two_button,
            self.array_test_three_button,
            self.createArrayButton,
            self.removeArrayButton,
            self.sortArrayButton,
        ]

        for button in buttons:
            self.layout.addWidget(button)

        logging.debug("buttons added to window layout from show_buttons_in_layout")
        
    # Getter and Setter for array_list _________________________________________________________________
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

    # Button Functions ____________________________________________________________________
    @Slot()
    def create_array_function(self):
        try:
            self.create_and_assign_array()
            logging.info("Array created successfully.")
        except Exception as e:
            logging.error(f"Error creating array: {e}")

    @Slot()
    def remove_array(self):
        self._client_count = 0
        self._client_data_records = None
        msg = "Array has been erased"
        show_message_box("Array Removed", msg)

    @Slot()
    def sort_array(self):
        show_message_box("Under Construction")

    @Slot()
    def array_test_one_a(self):
        """
        Runs Test Number One, Part A.

        This function checks for an existing array and creates a new one
        if necessary, then runs Test Number One.
        """
        logging.debug("Running Test One, Creating Array!")
        numofClients, funWithArrays, clientRecords = createArray()

        # Use setters to assign values
        self.array_list = funWithArrays
        self.client_count = numofClients
        self.client_data_records = clientRecords
        elapsedTime = testNumberOne(numofClients, funWithArrays, clientRecords)

        message= (
                f"Clients have been successfully added!\n\nTerminal Output:"
                f"\nTime taken to add {self._client_count} client records:\n"
                f"{elapsedTime:.6f} seconds"
                )
        show_message_box("Action Completed", message)

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


    @Slot()
    def array_test_three(self):
        
        # Proceed if checkForExistingArray returned True
        logging.info("Running Test Three!")

        # Add records
        numofClients, funWithArrays, clientRecords = createArray()
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

    # Helper functions, could be seperated later _______________________________________________
    def check_for_array(self):
        """
        Checks if an array exists; prompts the user if not.
        """
        if not checkForExistingArray(self._client_count, self._array_list):
            message = ("Please click the create array button before running this test")
            show_message_box("Error: No existing array.", message)
            # Exit the function early if check fails
            return False
        else:
            return True
        
    def create_and_assign_array(self):
        """
        Creates an array and runs a test on it.

        This function initializes a new array, checks if an existing array
        exists, and then runs Test Number One.
        """
        numofClients, funWithArrays, clientRecords = createArray()

        # Use setters to assign values
        self.array_list = funWithArrays
        self.client_count = numofClients
        self.client_data_records = clientRecords
        
        logging.info("\nCreating Array!\nArray Created successfully!")