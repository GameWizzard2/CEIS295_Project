# Name: Christopher Barfield
# Date: 11/23/2024

from BubbleSort import BubbleSort
from InsertionSort import InsertionSort
from MergeSort import MergeSort
from Quicksort import Quicksort
from SelectionSort import SelectionSort
from ShellSort import ShellSort
from Client import Client
import time
from datetime import date

import os


def create_client_records(inputFileName):
    """
    Reads client data from a CSV file and creates client objects.

    Args:
        inputFileName (str): The path to the CSV file containing client data.

    Returns:
        list: A list of Client objects created from the CSV data.
    """
    clientRecords = []
    with open(inputFileName, 'r') as infile:
        for line in infile:
            s = line.strip().split(',')  # Strip removes any trailing newline characters
            client_id = int(s[0])  # Convert the default string to an int
            f_name = s[1]
            l_name = s[2]
            phone = s[3]
            email = s[4]
            
            # Create a Client object using the data from the file
            clt = Client(client_id, f_name, l_name, phone, email)
            
            # Add the Client object to the list
            clientRecords.append(clt)
    return clientRecords


def create_array(inputFileName):
    """
    Reads client data from a CSV file and returns the number of clients and their records.

    Args:
        inputFileName (str): The path to the CSV file.

    Returns:
        tuple: Number of clients (int), list of Client objects.
    """
    clientRecords = create_client_records(inputFileName)
    numofClients = len(clientRecords)
    return numofClients, clientRecords


def main():
    print("Name:", "Christopher H Barfield")
    print("Date:", date.today())
    print('')

     # Base directory where the files are stored (relative to the main script)
    base_dir = os.path.join('.', 'Module_4')

    # List of CSV test files
    file_options = {
        1: os.path.join(base_dir, 'ClientData100.csv'),
        2: os.path.join(base_dir, 'ClientData1000.csv'),
        3: os.path.join(base_dir, 'ClientData10000.csv'),
        4: os.path.join(base_dir, 'ClientData100000.csv')
    }
    
    
    # Sorting algorithm options
    sort_options = {
        1: ('Bubble Sort', BubbleSort.sort),
        2: ('Insertion Sort', InsertionSort.sort),
        3: ('Merge Sort', MergeSort.sort),
        4: ('Quick Sort', Quicksort.sort),
        5: ('Selection Sort', SelectionSort.sort),
        6: ('Shell Sort', ShellSort.sort),
    }
    
    # Display file options to the user
    print("Select the input file:")
    for key, filename in file_options.items():
        print(f"{key}: {filename}")
    
    try:
        # User selects a file
        file_choice = int(input("Enter the number corresponding to your choice: "))
        inputFileName = file_options.get(file_choice, None)
        
        if not inputFileName:
            print("Invalid file choice. Please run the program again and select a valid option.\nClosing program...")
            return

        # Print chosen file
        print(f"\nFilename chosen: {inputFileName}... Running...\n")
        time.sleep(2)

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

        # Create client records
        numofClients, clientRecords = create_array(inputFileName)
        sectionTitle = f"Scenario: Sorting {numofClients} records using {sort_name}."
        print(f"{sectionTitle}\n{60 * '_'}")

        # Perform sorting
        startTime = time.time()
        sort_function(clientRecords)
        endTime = time.time()
        elapsedTime = endTime - startTime
        print(f"Time taken to sort {numofClients} records using {sort_name}: {elapsedTime:.6f} seconds\n\nSee sorted records below:\n")

        # Print sorted client records
        for clt in clientRecords:
            print(clt)
        print(f"For reference---\nTime taken to sort {numofClients}: {elapsedTime:.6f} seconds")

    except ValueError:
        print("Invalid input. Please enter a number corresponding to the choices.\nClosing program...")
        time.sleep(2)


if __name__ == '__main__':
    main()
