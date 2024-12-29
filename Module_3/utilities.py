# Local imports
from Queue import Queue
from Call import Call

# Built-in
import sys

def createCallQueue(newList = []):
    """    
    Create a call queue from a CSV file containing call information.

    This function reads call data from a CSV file, creates Call objects using the extracted
    information, and appends them to a list representing the call queue.

    Args:
        newList (list, optional): A list to store the Call objects. Defaults to an empty list.

    Returns:
        list: The updated list containing Call objects created from the file data.

    File Input:
        The function reads data from a CSV file named 'Module_2/ClientData.csv'.
        The file format expects the following columns:
            - Client ID (int)
            - Customer Name (str)
            - Customer Phone (str)
    """
    input_file_name = '.\Module_2\ClientData.csv'
    with open(input_file_name) as infile:
        for line in infile:
            s = line.split(',')
            clientId = int(s[0])  # convert the default string to an int
            customerName = s[1]
            customerPhone = s[2]
            # Create a Call object based on the line from the file.
            callQueue = Call(clientId, customerName, customerPhone)
            # Add the call object to the list
            newList.append(callQueue)
        return newList
    
def userContinueInput():
    print("Press \"Enter\" to continue...")
    sys.stdin.read(1)  # Reads one character (like Enter) from standard input