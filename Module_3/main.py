# Local
from Queue import Queue
from AutomaticCallDistributor import automatedCallCenterTest
from utilities import (
    createCallQueue,
    userContinueInput,
)
# Built-in
from datetime import date

def main():
    print("Name:", "Christopher H Barfield")
    print("Date:", date.today())
    userContinueInput()
    callQueueList = createCallQueue()
    callWaiting = Queue()
    automatedCallCenterTest(callQueueList, callWaiting)


if __name__ == "__main__":
    main()