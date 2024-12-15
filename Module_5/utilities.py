# local
from Client import Client
# built-in
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

def file_options():
    # Base directory where the files are stored (relative to the main script)
    base_dir = os.path.join('.', 'Module_4')

    # List of CSV test files
    return {
        1: ('ClientData100',os.path.join(base_dir, 'ClientData100.csv')),
        2: ('ClientData1000',os.path.join(base_dir, 'ClientData1000.csv')),
        3: ('ClientData10000',os.path.join(base_dir, 'ClientData10000.csv')),
        4: ('ClientData100000',os.path.join(base_dir, 'ClientData100000.csv'))
    }


def display_file_options():

    # Display file options to the user
    print("Select the input file:")
    for key, (displayName, filePath) in file_options().items():
        print(f"{key}: {displayName}")

def user_pick_file():
    try:
        # User selects a file
        file_choice = int(input("Enter the number corresponding to your choice: "))
        if len(file_options()) < file_choice:
            return False
        else:
            return file_options().get(file_choice, (None,None))
    
    except ValueError:
        print("Invalid file choice. Please run the program again and select a valid option.\nClosing program...")
        return False

def user_rerun_section():
        while True:
            userInput = input("\n\nRerun program????? Input:y/n:\n")
            if userInput in ["y","Y"]:
                return True
            elif userInput in ["n","N"]:
                print("....stopping execution")
                return False
            else:
                print("Invalid input, must be:\nMust be 'y' or 'n'.\n\n")