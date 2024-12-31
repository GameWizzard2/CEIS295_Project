# Built-in
import sys
import logging

# Third Party
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
from PySide6.QtCore import Slot

# Local Imports

class MainWindow():
    """
    A GUI application for interacting with array operations using PySide6.

    This class creates a PySide6-based GUI with buttons to open
    different sub-windows.
    """
    def __init__(self):
        """
        Initializes the GUI application and its components.
        """
        
        # Create the Qt Application
        self.app = QApplication(sys.argv)

        # Create a main window to hold widgets.
        self.window = QWidget()
        self.layout = QVBoxLayout()

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
        # Run the main Qt loop
        self.app.exec()

    

MainWindow().run()