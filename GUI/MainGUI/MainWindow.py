# Built-in
import sys
import logging

# Third Party
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
from PySide6.QtCore import Slot

# Local Imports
from GUI.Module_1.ArrayGUI import ArrayGUI


class MainWindow(QWidget):
    """
    A GUI application for interacting with array operations using PySide6.

    This class creates a PySide6-based GUI with buttons to open
    different sub-windows.
    """
    def __init__(self):
        """
        Initializes the GUI application and its components.
        """
        super().__init__()

        # Create a main layout for the window
        self.layout = QVBoxLayout(self)

        # Initialize buttons
        self.init_buttons()

        # Set up the layout and window title
        self.setLayout(self.layout)
        self.setWindowTitle("Project App")

    def init_buttons(self):
        """Initialize all buttons."""
        self.array_tests_button = QPushButton("Array Test Functions")
        self.layout.addWidget(self.array_tests_button)

        # Connect the button click to the corresponding slot
        self.array_tests_button.clicked.connect(self.call_array_window)

    @Slot()
    def call_array_window(self):
        """
        Opens the ArrayGUI window when the button is clicked.
        """
        self.array_gui = ArrayGUI(self)  # Pass the parent
        self.array_gui.show()
        logging.info("Array opened successfully.")