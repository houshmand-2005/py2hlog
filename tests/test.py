import sys
import os
ERROR_COUNTER = -1
sys.path.insert(0, '..')


def error_found(error="", error_counter=False):
    global ERROR_COUNTER
    ERROR_COUNTER += 1
    if error_counter:
        print("-------------------------")
        print("Total number of errors : ", ERROR_COUNTER)
    else:
        print("-------------------------")
        print(error)


try:
    from src.py2hlog import logger
    from src.py2hlog import html_files
    from src.py2hlog import addtree
except ModuleNotFoundError as ex:
    print(ex)
    error_found('*** Go to test folder ./tests ***')

try:
    obj1 = logger.py2hlog()
    print("print obj1: ", obj1)
except Exception as ex:
    print(ex)
    error_found("Cannot call the function")

try:
    obj1.file_name = "new_log_file.txt"
    obj1.debug("your message")
    obj1.makehtml("py2hlog.html")
except Exception as ex:
    print(ex)
    error_found('Cant make html file')

try:
    obj1.critical("Py2hlog", 13, 16)
    obj1.debug("Py2hlog", 13, 16)
    obj1.info("Py2hlog", 13, 16)
    obj1.warning("Py2hlog", 13, 16)
    obj1.error("Py2hlog", 13, 16)
except Exception as ex:
    print(ex)
    error_found('It does not show the line that has a problem')

try:
    obj1.critical("your message")
    obj1.debug("your message")
    obj1.info("your message")
    obj1.warning("your message")
    obj1.error("your message")
except Exception as ex:
    print(ex)
    error_found('The log is not written')

try:
    obj1._add_time_and_caller_file("hello")
except Exception as ex:
    print(ex)
    error_found("It cannot insert the time and location of the executable file.")

try:
    obj1._write_log("new", "Hi")
except Exception as ex:
    print(ex)
    error_found("Can't add log level and message and cant open the file")

try:
    obj1._ch_lines(1, 4)
except Exception as ex:
    print(ex)
    error_found("Cannot find the specified section")

try:
    os.remove("new_log_file.txt")
    os.remove("py2hlog.html")
except:
    pass

error_found("", True)
