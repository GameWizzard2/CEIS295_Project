# Built-in
import sys
import logging

# Third Party
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QLabel, QMainWindow
from PySide6.QtCore import Slot

# Local Imports
from GUI.Module_1.ArrayGUI import ArrayGUI


class MainWindow(QMainWindow):
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

        # Set the main window title
        self.setWindowTitle("Main GUI")

        # Set up the central widget and layout
        central_widget = QWidget(self)  # Create a central widget
        self.setCentralWidget(central_widget)  # Set it as the central widget
        self.layout = QVBoxLayout(central_widget)  # Set the layout

        # Add a title label
        title_label = QLabel("Tests:")
        title_label.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 10px;")
        self.layout.addWidget(title_label)

        # Initialize buttons
        self.init_buttons()

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
        self.array_gui = ArrayGUI()  # Pass the parent
        self.array_gui.show()
        logging.info("ArrayGUI window opened successfully.")


if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO)

    # Create the application
    app = QApplication(sys.argv)

    # Create and show the main window
    main_window = MainWindow()
    main_window.show()

    # Run the application
    sys.exit(app.exec())
