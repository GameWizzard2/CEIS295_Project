# Name: Christopher H Barfield
# Date: 2024-16-07
from datetime import date
import time
import random
import sys



def automatedCallCenterTest(callQueueList, callWaiting ):
    """
    8.	Ask the user for the number of seconds to run the simulation. Create a for loop that will run one time for each second that was inputted. In the for loop, take these steps:

    a.	Pause the application for two seconds using time.sleep(2)
    b.	Generate a random number from 1 to 3
    c.	If the random number is 1, add a call to the call_waiting queue and then increment the call_number variable. Then, show how many calls are currently in the call_waiting queue.
    d.	Otherwise, if the randomly generated number is 2, remove a call from the call_waiting queue and tell the user that the call is being routed to a service representative. Display the call’s information. Then, show how many calls are currently in the call_waiting queue.
    e.	Otherwise, do nothing to the queue. Tell the user that nothing happened during this second of time. Then, show how many calls are currently in the call_waiting queue.
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
