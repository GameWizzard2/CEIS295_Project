#Name: Christopher Barfield
#Date:  11/26/2024

from LinearSearch import LinearSearch
from BinarySearch import BinarySearch
from Quicksort import Quicksort
from Client import Client

from datetime import date
import random
import time
import os

def begin_linear_search_test(numofClients, clientRecords):

    startTime = time.time()
    startRecord = 100001
    endRecord = startRecord + numofClients
    # search for 1000 random records
    for i in range(1000):
        clientID = random.randint(startRecord,endRecord)
        clt = Client(clientID)
        result = LinearSearch.search(clientRecords,clt)
        if result is None:
            print(f"{clt}: was not found.")
        else:
            print(result)
            endTime = time.time()
            elapsedTime = endTime - startTime
    print(f"The total time to search 1000 records using the linear search algorithm with {numofClients} records was {elapsedTime:.6f}")

def begin_binary_search_test(numofClients, clientRecords):

    startTime = time.time()
    startRecord = 100001
    endRecord = startRecord + numofClients
    # search for 1000 random records
    for i in range(1000):
        clientID = random.randint(startRecord,endRecord)
        clt = Client(clientID)
        result = BinarySearch.search(clientRecords,clt)
        if result is None:
            print(f"{clt}: was not found.")
        else:
            print(result)
            endTime = time.time()
            elapsedTime = endTime - startTime
    print(f"The total time to search 1000 records using the Binary search algorithm with {numofClients} records was {elapsedTime:.6f}")

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

def file_options():
    # Base directory where the files are stored (relative to the main script)
    base_dir = os.path.join('.', 'Module_4')

    # List of CSV test files
    return {
        1: os.path.join(base_dir, 'ClientData100.csv'),
        2: os.path.join(base_dir, 'ClientData1000.csv'),
        3: os.path.join(base_dir, 'ClientData10000.csv'),
        4: os.path.join(base_dir, 'ClientData100000.csv')
    }


def display_file_options():

    # Display file options to the user
    print("Select the input file:")
    for key, filename in file_options().items():
        print(f"{key}: {filename}")

def user_pick_file():
    try:
        # User selects a file
        file_choice = int(input("Enter the number corresponding to your choice: "))
        if len(file_options()) < file_choice:
            return False
        else:
            inputFileName = file_options().get(file_choice, None)
            return inputFileName
    
    except ValueError:
        print("Invalid file choice. Please run the program again and select a valid option.\nClosing program...")
        return False

def user_rerun_section():
        while True:
            userInput = input("\n\nRerun program????? Input:y/n")
            if userInput in ["y","Y"]:
                return True
            elif userInput in ["n","N"]:
                print("....stopping execution")
                return False
            else:
                print("Invalid input, must be:\nMust be 'y' or 'n'.\n\n")

def main():
    flag = True
    while flag:
        print("Name:", "Christopher H Barfield")
        print("Date:", date.today())

        display_file_options()
        fileName = user_pick_file()

        # Print chosen file
        if fileName is not False:
            print(f"\nFilename chosen: {fileName}... Running...\n")
            time.sleep(2)
        else:
            print("\nplease re-run program and choose a valid option")

        # Create client records
        numofClients, clientRecords = create_array(fileName)
        sectionTitle = f"Scenario: Sorting {numofClients} records using Quicksort."
        print(f"{sectionTitle}\n{60 * '_'}")

        # Sort records. WARNING: Records must be sorted for binary search to work correctly
        Quicksort.sort(clientRecords)


        #TODO make this callable. # Begin linear timed search test
        begin_linear_search_test(numofClients, clientRecords)

        #TODO make this callable. # Begin Binary timed search test
        #begin_binary_search_test(numofClients, clientRecords)
        
        flag = user_rerun_section()
        
        



    
    

if __name__ == '__main__':
    main()