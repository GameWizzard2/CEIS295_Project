# Local
from SortingActualSpeeds import (
    user_selects_file,
    user_selects_Sorting_algo,
    sorting_speeds_test
)
from utilities import create_array

# Built-in
from datetime import date
import time

def main():
    print("Name:", "Christopher H Barfield")
    print("Date:", date.today())
    try:
        chosenFile = user_selects_file()
        sort_name, sort_function = user_selects_Sorting_algo()

        # Create client records
        numofClients, clientRecords = create_array(chosenFile)
        sectionTitle = f"Scenario: Sorting {numofClients} records using {sort_name}."
        print(f"{sectionTitle}\n{60 * '_'}")

        # Perform test
        sorting_speeds_test(sort_function, sort_name, numofClients, clientRecords)

    except ValueError:
        print("Invalid input. Please enter a number corresponding to the choices.\nClosing program...")
        time.sleep(2)

if __name__ == "__main__":
    main()