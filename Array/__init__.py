# __init__.py
# Description: Package Initialization
# Author: Christopher Barfield
# Date: 11/2/2024

# Import core functionalities into the package namespace
from .ArrayList import ArrayList
from .ArrayListActualSpeed import (
    testNumberOne, 
    testNumberOneContinued,
    testNumberTwo,
    testNumberThree,
)
from .Utilities import (
    appendToArray,
    remove_from_array,
    create_client_records,
    createArray,
    checkForExistingArray,
)


# Define __all__ to control what gets imported with 'from package import *'
__all__ = [
    "ArrayList",
    "testNumberOne",
    "testNumberOneContinued",
    "testNumberTwo",
    "testNumberThree",
    "appendToArray",
    "remove_from_array",
    "create_client_records",
    "createArray",
    "checkForExistingArray",
]
