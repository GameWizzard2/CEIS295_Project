# local
from Client import Client
from ArrayList import ArrayList

# built-in
import sys

def appendToArray(numofClients, clientRecords):
    """
    Append clientRecords to an array object
    """
    arrayList = ArrayList()
    for i in range(numofClients):
        arrayList.append(clientRecords[i])
    return arrayList

def createClientRecords(clientRecords):
    input_file_name = '.\Module_1\ClientData.csv'
    with open(input_file_name) as infile:
        for line in infile:
            s = line.split(',')
            client_id = int(s[0])  # convert the default string to an int
            f_name = s[1]
            l_name = s[2]
            phone = s[3]
            email = s[4]
            
            # create a client object using the data from the file
            clt = Client(client_id, f_name, l_name, phone, email)
            
            # add the client object to the list
            clientRecords.append(clt)

    return clientRecords

def userContinueInput():
    print("Press \"Enter\" to continue...")
    sys.stdin.read(1)  # Reads one character (like Enter) from standard input