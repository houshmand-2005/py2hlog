# py2hlog (Python to HTML log)
see it from pypi [pypi.org/project/py2hlog/](https://pypi.org/project/py2hlog/)

Python logs to HTML formatter

install py2hlog:
```bash
pip install py2hlog
```

simple useage :
```bash
from py2hlog import logger
import time
obj1 = logger.py2hlog()  # create an object from py2hlog
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
# you can also use these statuses :
# _____________________________
# obj1.critical("your message")
# obj1.debug("your message")
# obj1.info("your message")
# obj1.warning("your message")
# obj1.error("your message")
# _____________________________

```
**py2hlog.html** output : 

<img src="https://github.com/houshmand-2005/py2hlog/blob/ec6f99679990a0fd1d585ff8ccf261ae9cac0d22/images/1.jpg" alt="randomazer_hash" width="700">

All of the statuses:

<img src="https://github.com/houshmand-2005/py2hlog/blob/5a5f6cc5c5f0002c56d98b4621c77b7aa1af3c16/images/3.png" alt="randomazer_hash" width="700">

You can also see which file the log belongs to and when the log was added. like this:

<img src="https://github.com/houshmand-2005/py2hlog/blob/ec6f99679990a0fd1d585ff8ccf261ae9cac0d22/images/2.jpg" alt="randomazer_hash" width="700">

**THIS IS BETA VERSION**

houshmand2005
