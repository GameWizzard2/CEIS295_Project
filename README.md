# CEIS295_Project_Modified

This project provides a detailed analysis and performance testing of various data structure operations on an **ArrayList** of client records. It simulates real-world scenarios in customer service centers and call centers to evaluate the efficiency of **array-based data structures** for managing client data, all at the click of a button using a GUI interface.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [How to Run](#how-to-run)
- [Code Modules](#code-modules)
- [Contributing](#contributing)
- [Author](#author)

---

## Project Overview

This project tests the following key functionalities:

1. **Client Record Management**: Creation, sorting, appending, and testing operations on client records.
2. **Performance Testing**: Evaluating the efficiency of array-based operations through custom test cases.
3. **Sorting Algorithm**: Implemented and tested **Quicksort** for sorting client records.
4. **Logger and GUI Support**: Custom logger for detailed runtime logs and a simple GUI application.

---

## Features

- Create and manage an **ArrayList** of client records.
- Sort client records using the **Quicksort** algorithm (with future optional support).
- Test multiple array operations, including:
   - Append new client data.
   - Performance and integrity checks.
   - Deletion and verification tests.
- Detailed logging through a custom logger.
- **GUI Application** interface for user interaction (using PySide6).

---

## Technologies Used

- **Python**: Core language for implementing logic.
- **PySide6**: For building a simple GUI application.
- **Logging Module**: For recording runtime data.
- **Quicksort**: Custom implementation for sorting algorithms.
- **datetime**: To display the current date.

---

## How to Run

Follow these steps to run the project:

1. Clone this repository:
   ```bash
   'git clone https://github.com/GameWizzard2/CEIS295_Project.git'

2. Navigate to the repository:
   'cd CEIS295_Project'

3. Create and activate virtual enviroment:

    **Windows**
    'python -m venv venv'
    '.\venv\Scripts\activate'


4.  Install dependencies:
    'pip install -r requirements.txt'

4.  Activate GUI:
    python main.py

## Code Modules

The project is organized into the following modules:

### Array Package (`Array`)

The `Array` folder is a Python package that contains multiple modules for handling client records and array-based operations.

#### **Modules**:

1. **`ArrayList.py`**:

   - 'Array()': Generates an array object to pass a list of vlient information into.
   - **Test Functions**:
     - `testNumberOne()`
     - `testNumberOneContinued()`
     - `testNumberTwo()`
     - `testNumberThree()`

2. **`ArrayListActualSpeed.py`**:
    - Contains performance benchmarking functions for measuring the actual execution speed of array operations.
    - `testNumberOne()`
    - `testNumberOneContinued()`
    - `testNumberTwo()`
    - `testNumberThree()`

3. **`__init__.py`**:
   - Initializes the `Array` package and allows the modules to be imported as part of the package.

---

### Logger Module (`Logger.py`):

- `CustomLogger.main()`: Setup a logging system to track runtime behavior.

### Sorting Module (`SortingAlgo.py`):

- **Quicksort** implementation for sorting client records.

### GUI Module (`GUI.py`):

- `ProjectApp`: A PySide6 based GUI for better user interaction.

### Main Script:

- Runs the entire project, combining logging, data handling, and GUI.

---
## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.  
2. Create a feature branch:  
   ```bash
   git checkout -b feature-branch

---

## Author
**Christopher H Barfield**
Bachelor of Science in Software Development

Email: YourEmail@example.com
GitHub: https://github.com/GameWizzard2






