import logging
import os

def setup_logging():
    """
    Sets up logging configuration for both file and console output.

    This function initializes logging with a specified log file, setting the file log level to DEBUG
    and the console log level to ERROR. The log format includes information such as timestamp, filename, 
    logger name, log level, line number, and the log message.

    Returns:
        str: The filename of the log file.
    """
    # Log file name
    log_file = 'log_info.log'

    # Configure logging to file with DEBUG level for detailed logging
    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,
        format='%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s'
    )

    # Configure logging to console for ERROR level messages and above
    console = logging.StreamHandler()
    console.setLevel(logging.ERROR)  # Console will only show errors
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)

    # Add the console handler to the root logger
    logging.getLogger(__name__).addHandler(console)

    # Log an initial message to ensure the log file is created immediately
    logging.info("Logging setup complete. Log file initialized.")

    return log_file

def create_log(log_file):
    """
    Prints the absolute path of the log file and checks if it was successfully created.

    Args:
        log_file (str): The filename of the log file.
    """
    # Get absolute path of the log file
    log_file_path = os.path.abspath(log_file)

    # Print where the log file is located
    print(f"Log file will be created at: {log_file_path}")

    # Check if the log file exists and print appropriate message
    if os.path.exists(log_file_path):
        print(f"Log file '{log_file_path}' created successfully.")
    else:
        print(f"Failed to create log file '{log_file_path}'.")

def main():
    """
    Main function that sets up logging and creates the log file.

    This function initializes the logging system, verifies the log file creation, and logs a test message.
    """
    # Set up logging and retrieve the log file name
    log_file = setup_logging()

    # Check the log file path and creation status
    create_log(log_file)

    # Log a test message to confirm logging is working
    logging.debug('Test message logged.')


#main()

"""# Re-export logging functions for convenience
debug = logging.debug
info = logging.info
warning = logging.warning
error = logging.error
critical = logging.critical"""