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

Also you can mark a part of your code for each status like this:

```bash
from py2hlog import logger
object_of_py2hlog = logger.py2hlog()
object_of_py2hlog.file_name = "Py2hlog.txt"
object_of_py2hlog.warning("you can also mark a part of code for this status like -->", 1, 5)
# ("msg", start line, end line)
object_of_py2hlog.makehtml("Py2hlog.html")
```

output : 

<img src="https://github.com/houshmand-2005/py2hlog/blob/8cd72d49c5627b604a204603225743416c011050/images/V0.3.jpg" alt="randomazer_hash" width="700">

As you can see, when you click on 'see code', the codes will appear<br>
<br>
what is new :
<br>✨ Add the ability to show the contents of the executable file folder and display it
<br><img src="https://github.com/houshmand-2005/py2hlog/blob/47d372b037abee1f99b1a70bd14f16ad9b9e0719/images/4.1.png" alt="newabli" width="700">
<br>
<br>
✨After the last update(V1.2) we have a better style for tree:<br>
 &emsp; Before &emsp;&emsp;&emsp;&emsp;&emsp;&emsp; After
<div style="display: flex;">
  <img src="https://github.com/houshmand-2005/py2hlog/blob/47d372b037abee1f99b1a70bd14f16ad9b9e0719/images/4.3.png" alt="newabli" width="120" height="270">
  <img src="https://github.com/houshmand-2005/py2hlog/blob/47d372b037abee1f99b1a70bd14f16ad9b9e0719/images/4.2.png" alt="newabli" width="120" height="270">
</div>

<hr>
houshmand2005
