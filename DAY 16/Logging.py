import logging
logging.info("User Logged in")

logging.basicConfig(level=logging.DEBUG)
logging.debug("Debug Message")
logging.info("Program Started")
logging.warning("Low Memory")
logging.error("File Not Found")
logging.critical("System Crash")

logging.basicConfig(
    filename="app.log",
    level=logging.info
    )
logging.info("Application Started")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Student Login")

try:
    10/0
except Exception:
    logging.exception("Exception occurred")
    
logging.basicConfig(level=logging.WARNING)


import logging
import os

# 1. Configure logging with a custom format, level threshold, and file output
logging.basicConfig(
    level=logging.INFO,  # Displays INFO and above (ignores DEBUG)
    filename="student.log",
    filemode="w",  # 'w' overwrites the file each run; use 'a' to append
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# 2. Compare print() and logging (Console vs File/Structure demonstration)
print("--- Console Output (print vs logging) ---")
print("This is a standard print statement for tracking.")
# Note: Since logging is configured to a file, the following lines write to 'student.log'
logging.info("This is an INFO log message tracking program flow.")

# 3. Print one message using each logging level
# DEBUG will be ignored because the threshold is set to INFO
logging.debug("DEBUG: This will NOT appear in the log file.")
logging.info("INFO: Student system initialized successfully.")
logging.warning("WARNING: Low disk space on the logging server.")
logging.error("ERROR: Failed to connect to the student database.")
logging.critical("CRITICAL: System shutting down due to unhandled panic.")


# 4. Program feature: Log student login attempts
def log_login_attempt(username, success):
    if success:
        logging.info(f"Login SUCCESS: User '{username}' logged in.")
    else:
        logging.warning(f"Login FAILED: Unauthorized attempt for user '{username}'.")


# 5. Program feature: Log a warning when marks are below 35
def check_student_marks(student_name, marks):
    if marks < 35:
        logging.warning(
            f"ACADEMIC ALERT: {student_name} scored {marks}/100 (Below passing threshold of 35)."
        )
    else:
        logging.info(f"ACADEMIC PASS: {student_name} passed with {marks}/100.")


# 6. Program feature: Log an error if a file cannot be opened
def read_student_profile(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError as e:
        logging.error(f"FILE ERROR: Cannot open '{filename}'. Details: {e}")


# 7. Program feature: Log a division-by-zero exception
def calculate_average_score(total_marks, total_students):
    try:
        return total_marks / total_students
    except ZeroDivisionError:
        # logging.exception automatically appends the full stack trace
        logging.exception("MATH ERROR: Attempted to divide total marks by zero students.")


# --- Execute the Program Scenarios ---
log_login_attempt("alex_99", True)
log_login_attempt("unknown_user", False)

check_student_marks("John Doe", 78)
check_student_marks("Jane Smith", 28)

read_student_profile("non_existent_report.txt")

calculate_average_score(450, 0)

print("Program execution finished. Check 'student.log' to view the formatted logs.")
   
    
import logging
import sys

# 1. Configure logging to write to student_result.log with a custom format
logging.basicConfig(
    level=logging.INFO,
    filename="student_result.log",
    filemode="a",  # 'a' appends new logs to the file without deleting old entries
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def process_student_data():
    print("--- Student Data Entry System ---")

    # Step 1: Input Student Name
    name = input("Enter student name: ").strip()
    if not name:
        logging.critical("CRITICAL: Invalid data type or empty value for name.")
        print("Error: Student name cannot be empty. Check log for details.")
        return

    # Step 2: Input and Validate Student Marks
    raw_marks = input(f"Enter marks for {name}: ").strip()

    try:
        # Check if the data type can be converted to a float/number
        marks = float(raw_marks)
    except ValueError:
        # CRITICAL -> Fails data type integrity
        logging.critical(
            f"CRITICAL: Invalid data type entered for marks. Input received: '{raw_marks}'"
        )
        print("Data Type Error: Marks must be a number. Check log for details.")
        return

    # Step 3: Evaluate Marks Range and Thresholds
    # ERROR -> Out of valid academic bounds
    if marks < 0 or marks > 100:
        logging.error(
            f"ERROR: Invalid marks entered for {name}. Value {marks} is out of bounds (0-100)."
        )
        print("Range Error: Marks must be between 0 and 100. Check log for details.")

    # WARNING -> Academic failure risk
    elif marks < 35:
        logging.info(f"INFO: Student details entered successfully for {name}.")
        logging.warning(
            f"WARNING: {name} scored {marks}/100, which is below the passing threshold of 35."
        )
        print(f"Data recorded. Warning logged for low marks ({marks}).")

    # INFO -> Standard successful process
    else:
        logging.info(
            f"INFO: Student details entered. {name} passed successfully with {marks}/100."
        )
        print(f"Success: Data for {name} successfully processed and logged.")


if __name__ == "__main__":
    process_student_data()

    
    
    
    
