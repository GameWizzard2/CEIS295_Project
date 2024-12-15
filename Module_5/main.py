# local

from utilities import (
    display_file_options,
    user_pick_file,
    create_array,
    user_rerun_section
)
from SearchingActualSpeed import (
    search_test_options
)
from Quicksort import Quicksort
# built-in
import time
from datetime import date
def main():
    flag = True
    while flag:
        print("Name:", "Christopher H Barfield")
        print("Date:", date.today())

        display_file_options()
        displayName, fileName = user_pick_file()

        # Print chosen file
        if fileName is not False:
            print(f"\nFilename chosen: {displayName}... Running...\n")
            time.sleep(2)
        else:
            print("\nplease re-run program and choose a valid option")

        # Create client records
        numofClients, clientRecords = create_array(fileName)
        sectionTitle = f"Scenario: Sorting {numofClients} records using Quicksort."
        print(f"{sectionTitle}\n{60 * '_'}")

        # Sort records. WARNING: Records must be sorted for binary search to work correctly
        Quicksort.sort(clientRecords)

        displayName, searchFunction = search_test_options()


        #TODO make this callable. # Begin linear timed search test
        searchFunction(numofClients, clientRecords)

        #TODO make this callable. # Begin Binary timed search test
        #begin_binary_search_test(numofClients, clientRecords)
        
        flag = user_rerun_section()
        
        



    
    

if __name__ == '__main__':
    main()