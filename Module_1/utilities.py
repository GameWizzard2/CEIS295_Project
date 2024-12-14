# local
from Client import Client
from ArrayList import ArrayList

# built-in
import sys

def appendToArray(numofClients, clientRecords):
    """
    Append client records to an ArrayList.

    This function initializes an ArrayList and appends a specified number of 
    client records to it.

    Args:
        numofClients (int): The number of client records to append.
        clientRecords (list): A list containing Client objects.

    Returns:
        ArrayList: An ArrayList containing the appended client records.
    """
    arrayList = ArrayList()
    for i in range(numofClients):
        arrayList.append(clientRecords[i])
    return arrayList


def createClientRecords(clientRecords):
    """
    Populate client records from a CSV file.

    This function reads client data from a CSV file, parses each line to create
    Client objects, and appends them to the provided list.

    Args:
        clientRecords (list): An empty list where Client objects will be added.

    Returns:
        list: The updated list containing Client objects.

    File Input:
        Module_1/ClientData.csv: A CSV file with the following columns:
            - Client ID (int)
            - First Name (str)
            - Last Name (str)
            - Phone Number (str)
            - Email Address (str)
    """
    input_file_name = './Module_1/ClientData.csv'
    with open(input_file_name) as infile:
        for line in infile:
            s = line.split(',')
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


def userContinueInput():
    """
    Pause program execution until user input.

    This function prompts the user to press "Enter" to continue, providing 
    a simple way to pause execution.

    Prints:
        A message asking the user to press "Enter".

    Input:
        Reads one character from the user (e.g., pressing Enter).
    """
    print('Press "Enter" to continue...')
    sys.stdin.read(1)  # Reads one character (like Enter) from standard input
