# Name: Christopher Barfield
# Date: 11/23/2024

# local
from BubbleSort import BubbleSort
from InsertionSort import InsertionSort
from MergeSort import MergeSort
from Quicksort import Quicksort
from SelectionSort import SelectionSort
from ShellSort import ShellSort

# built-in
import time
from datetime import date
import os

def user_selects_file():
    """
    Prompt the user to select an input file for processing.

    This function displays a list of available test files to the user, allows them
    to select one by entering a corresponding number, and retrieves the file path.

    Returns:
        str: The full file path of the selected file.

    Prints:
        A list of file options for the user to choose from and the selected filename.

    Raises:
        ValueError: If the user inputs a non-integer value.
    """
        # Base directory where the files are stored (relative to the main script)
    base_dir = os.path.join('.', 'Module_4')

    # List of CSV test files
    file_options = {
        1: ('ClientData100', os.path.join(base_dir, 'ClientData100.csv')),
        2: ('ClientData1000', os.path.join(base_dir, 'ClientData1000.csv')),
        3: ('ClientData10000', os.path.join(base_dir, 'ClientData10000.csv')),
        4: ('ClientData100000', os.path.join(base_dir, 'ClientData100000.csv'))
    }

    # Display file options to the user
    print("Select the input file:")
    for key, (display_name, _) in file_options.items():
        print(f"{key}: {display_name}")

    # User selects a file
    file_choice = int(input("Enter the number corresponding to your choice: "))
    chosenFile = file_options.get(file_choice, None)

    if not chosenFile:
        print("Invalid file choice. Please run the program again and select a valid option.\nClosing program...")
        return
    displayName, chosenFile = chosenFile 
    # Print chosen file
    print(f"\nFilename chosen: {displayName}... Running...\n")
    time.sleep(2)
    
    return chosenFile

def user_selects_Sorting_algo():
    """
    Prompt the user to select a sorting algorithm to use for sorting data.

    This function displays a list of available sorting algorithms, allows the user to
    select one, and returns the corresponding algorithm name and function.

    Returns:
        tuple: A tuple containing the selected sorting algorithm name (str) and function (callable).

    Prints:
        A list of sorting algorithms and the selected sorting algorithm name.

    Raises:
        ValueError: If the user inputs a non-integer value.
    """
    # Sorting algorithm options
    sort_options = {
        1: ('Bubble Sort', BubbleSort.sort),
        2: ('Insertion Sort', InsertionSort.sort),
        3: ('Merge Sort', MergeSort.sort),
        4: ('Quick Sort', Quicksort.sort),
        5: ('Selection Sort', SelectionSort.sort),
        6: ('Shell Sort', ShellSort.sort),
    }

    # Display sorting algorithm options
    print("Select the sorting algorithm:")
    for key, (name, _) in sort_options.items():
        print(f"{key}: {name}")
    
    # User selects a sorting algorithm
    sort_choice = int(input("Enter the number corresponding to your choice: "))
    sort_name, sort_function = sort_options.get(sort_choice, (None, None))
    
    if not sort_function:
        print("Invalid sorting algorithm choice. Please run the program again and select a valid option.\nClosing program...")
        return

    # Print chosen sorting algorithm
    print(f"\nSorting algorithm chosen: {sort_name}... Running...\n")
    time.sleep(2)

    return sort_name, sort_function

def sorting_speeds_test(sort_function, sort_name, numofClients, clientRecords): 
        """
        Measure and display the time taken to sort client records using a specified sorting algorithm.

        This function sorts a list of client records using the provided sorting function, measures the
        execution time, and displays the sorted records and time taken.

        Args:
        sort_function (callable): The sorting function to use for sorting the records.
        sort_name (str): The name of the sorting algorithm.
        numofClients (int): The number of client records to be sorted.
        clientRecords (list): A list of client records to sort.

        Returns:
        None

        Prints:
        - The time taken to sort the records.
        - The sorted client records.
        """
        sort_function(clientRecords)
        endTime = time.time()
        elapsedTime = endTime - startTime
        print(f"Time taken to sort {numofClients} records using {sort_name}: {elapsedTime:.6f} seconds\n\nSee sorted records below:\n")

        # Print sorted client records
        for clt in clientRecords:
            print(clt)
        print(f"For reference---\nTime taken to sort {numofClients}: {elapsedTime:.6f} seconds")