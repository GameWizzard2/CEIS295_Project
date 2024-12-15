# CEIS295 Course Project - Data Structures and Algorithms

## Project Overview
Data generated from a variety of sources, such as autonomous cars, call centers, mobile devices, social media, and websites, is growing exponentially. This project focuses on analyzing large datasets using different **data structures** and **sorting/searching algorithms**.

Through experimentation with various data structures and algorithms, this project demonstrates their **performance** and **real-world speeds** under different scenarios.

Each module in this project introduces and tests different data structures and algorithms, applying them to large datasets.

---

## Project Structure

The project is organized into **6 modules**, each covering specific data structures and algorithms. To execute each module, run the `main.py` file inside the respective folder.

### **Module 1: ArrayList and Quicksort**
- **Data Structures**: ArrayList  
- **Algorithms**: Quicksort  
- **Files**:
    - `ArrayList.py`: Implementation of ArrayList.
    - `Quicksort.py`: Sorting implementation using Quicksort.
    - `ClientData.csv`: Input data for testing.
    - `main.py`: Main file to execute sorting and speed tests.
    - `TimeProcess.py`: Measures execution time.
    - `utilities.py`: Utility functions.

---

### **Module 2: Linked List**
- **Data Structures**: Linked List  
- **Performance Measurement**: Real-world speeds under different scenarios.  
- **Files**:
    - `LinkedList.py`: Implementation of Linked List.
    - `LinkedListActualSpeed.py`: Speed measurement of Linked List operations.
    - `ClientData.csv`: Input data.
    - `TableofSpeedsWeek2.xlsx`: Performance results.
    - `main.py`: Main file to execute sorting and speed tests.

---

### **Module 3: Queue and Call Distributor**
- **Data Structures**: Linked List, Queue  
- **Real-World Scenario**: Call center management.  
- **Files**:
    - `Queue.py`: Implementation of Queue.
    - `AutomaticCallDistributor.py`: Simulates call distribution.
    - `ClientData.csv`: Input data.
    - `main.py`: Main file for simulation.

---

### **Module 4: Sorting Algorithms**
- **Algorithms**: BubbleSort, MergeSort, Quicksort, SelectionSort, ShellSort  
- **Objective**: Compare sorting speeds on datasets of increasing size.  
- **Files**:
    - `BubbleSort.py`: Bubble Sort implementation.
    - `MergeSort.py`: Merge Sort implementation.
    - `SelectionSort.py`: Selection Sort implementation.
    - `ClientData100.csv`, `ClientData1000.csv`, `ClientData10000.csv`: Input datasets of varying sizes.
    - `SortingActualSpeeds.py`: Measures sorting algorithm speeds.
    - `TableofRealWorldSortingSpeeds.xlsx`: Performance results.
    - `main.py`: Main file for sorting algorithm.

---

### **Module 5: Searching Algorithms**
- **Algorithms**: Binary Search, Linear Search  
- **Objective**: Measure and compare search speeds.  
- **Files**:
    - `BinarySearch.py`: Implementation of Binary Search.
    - `LinearSearch.py`: Implementation of Linear Search.
    - `SearchingActualSpeed.py`: Measures execution times.
    - `ClientData100.csv`, `ClientData1000.csv`, `ClientData10000.csv`: Input datasets.
    - `main.py`: Main file for searching Algorithm.

---

### **Module 6: Binary Search Tree**
- **Data Structures**: Binary Search Tree  
- **Objective**: Test speeds of Binary Search Tree operations.  
- **Files**:
    - `BinarySearchTree.py`: Binary Search Tree implementation.
    - `BinarySearchTreeListActualSpeed.py`: Measures speed of operations.
    - `ClientData.csv`: Input dataset.
    - `TableofSpeedsWeek6.xlsx`: Performance analysis results.
    - `main.py`: Main file for Binary Search Tree Tests.

---
## Project Outcome
### Key Learning Outcomes
- Hands-on experience with data structures: ArrayList, Linked List, Queue, Binary Search Tree.
- Implementation and comparison of sorting/searching algorithms:
- Sorting: Quicksort, MergeSort, BubbleSort, ShellSort, SelectionSort.
- Searching: Binary Search, Linear Search.
- Measuring algorithm speeds using real-world datasets.
- Optimizing applications based on experimental results.

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/GameWizzard2/CEIS295_Project.git
   cd CEIS295_Project

2. Check current Branch:
    ```bash
    git status

    'if in branch main continue.
    else:'

    git switch main 

3. Navigate to and run a specfic module:
    ```bash 
    cd Module_1
    python main.py
