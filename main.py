import sys

from PySide6.QtWidgets import QApplication
from Array import (create_client_records,
                   appendToArray,
                   ArrayList, 
                   testNumberOne, 
                   testNumberOneContinued,
                   testNumberTwo,
                   testNumberThree,
                   )
from GUI.MainGUI.MainWindow import MainWindow
from Logger import CustomLogger
from SortingAlgo import Quicksort
from datetime import date


def main():
    # Setup logger.
    CustomLogger.main() 
    # display name and date in output
    print("Name:", "Christopher H Barfield")
    print("Date:", date.today())

    clientRecords = []
    create_client_records(clientRecords)
    Quicksort.sort(clientRecords)
    funWithArrays = ArrayList()
    numofClients = len(clientRecords)
    testNumberOne(numofClients, funWithArrays, clientRecords)
    testNumberOneContinued(numofClients, funWithArrays, clientRecords)
    appendToArray(numofClients, funWithArrays, clientRecords)
    testNumberTwo(numofClients, funWithArrays, clientRecords)
    testNumberThree(numofClients, funWithArrays, clientRecords)

"class MyWidget(QtWidgets.QWidget):"


if __name__ == "__main__":
    CustomLogger.main()
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
