from Array import (
    createArray,
    appendToArray
)
class ArrayModel:
    """
    Handles array-related operations and data storage
    """
    def __init__(self):
        # Internal attributes for array data management
        self._array_list = None
        self._client_count = 0
        self._client_data_records = []
    
    def create_array(self, client_count, array_list, client_records):
        """
        Creates a new array and populates client data.
        """
        array_list, client_count, client_records = createArray()
        return appendToArray(client_count, array_list, client_records)