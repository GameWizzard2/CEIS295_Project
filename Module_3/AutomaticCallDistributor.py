# Name: Christopher H Barfield
# Date: 2024-16-07
from datetime import date
import time
import random

def automatedCallCenterTest(callQueueList, callWaiting ):
    """
        Simulate an automated call center queue over a user-defined duration.

        This function runs a simulation where calls are randomly added, removed, or left unchanged in a queue.
        The simulation pauses for two seconds on each iteration to mimic real-time behavior.

        Args:
            callQueueList (list): A list of calls that will be added to the call_waiting queue during the simulation.
            callWaiting (Queue): A queue data structure representing calls waiting to be serviced.

        Returns:
            None

        Simulation Steps:
            1. Prompt the user for the number of seconds to run the simulation.
            2. For each second in the simulation:
                a. Pause the program for 2 seconds using `time.sleep(2)`.
                b. Generate a random event (1, 2, or 3):
                    - If 1: Add a call to the queue and display the current queue length.
                    - If 2: Remove a call from the queue, display its details, and show the updated queue length.
                    - If 3: Do nothing and display the current queue length.
            3. Print a message indicating the end of the simulation.

        Prints:
            Status updates during each second of the simulation, including:
            - Calls added to the queue.
            - Calls removed and their details.
            - Current number of calls waiting in the queue.
            - Messages for no events occurring.
    """
    callNumber = 0
    # How long is the simulation
    userNumberOfSeconds = int(input("How many seconds should the simulation should run for? \nInput Number(Example - 12): "))

    for second in range(userNumberOfSeconds):
        print("-" * 40)
        time.sleep(2)
        randomEvent = random.randint(1, 3)
        # do the event based on the random generatored num
        if randomEvent == 1:
            print("Call Recieved, adding call to queue.")
            callWaiting.enqueue(callQueueList[callNumber])
            callNumber += 1 # Retrieve next call
            print(f"Current number of calls waiting:{callWaiting.get_length()}")

        elif randomEvent == 2:
            if callWaiting.get_length() > 0:
                print("Call sent to Service Representitive.")
                print(f"Call information\n{callWaiting.dequeue()}")
            else:
                print("The call list is currently empty!")
            print(f"Number of calls currently waiting in queue: {callWaiting.get_length()}")

        else:
            print("Nothing currently happening this second in time.")
            print(f"Number of calls currently waiting in queue: {callWaiting.get_length()}")
    print(f"{"-" * 40}\n<Automated Call Distributation Simulation Completed>")
