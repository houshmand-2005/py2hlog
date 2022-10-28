from main import py2hlog
import time
obj1 = py2hlog()  # create a object from py2hlog
obj1.file_name = "new_log_file.txt"  # here write the log detail
try:
    if a == 2:
        print("Iam working!")
except:
    obj1.error("I dont have any 'a' variable")
print("print obj1: ", obj1)
time.sleep(5)  # to see time changing
obj1.debug("Add a variable before the 'if' like a = 3")
obj1.makehtml("py2hlog.html")  # enter the name of output file
# you can also use this statuses :
# _____________________________
# obj1.critical("your message")
# obj1.debug("your message")
# obj1.info("your message")
# obj1.warning("your message")
# obj1.error("your message")
# _____________________________
