from Client import Client

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