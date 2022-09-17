import datetime
import inspect
from create_html_format import html_formater


class py2hlog():
    """main class -> here the functions we need called"""

    def __init__(self):
        self.file_name = None
        global caller
        caller = str(inspect.stack()[1][1])

    def __str__(self):
        return f"{self!r} in --> {self.file_name}"

    def _write_log(self, level, msg):
        """write log before transform to html"""
        path = self.file_name
        with open(path, "a") as log_file:
            log_file.write(f"[{level}] {msg}\n")

    def add_time_and_caller_file(self, msg):
        """add time for each log status"""
        now = str(datetime.datetime.now())
        msg += "<br><br><button type='button' class='btn btn-light' disabled> " + now + " </button>"
        msg += f"""
<br><br>
<div class='dropdown'>
  <a class='btn btn-secondary dropdown-toggle' href='#' role='button' data-bs-toggle='dropdown' aria-expanded='false'>From this File</a>
  <ul class='dropdown-menu'>
    <li class='dropdown-item'>{caller}</li>
  </ul>
</div>
"""
        return msg

    def critical(self, msg):
        """for critical log"""
        msg = py2hlog.add_time_and_caller_file(self, msg)
        self._write_log("CRITICAL", msg)

    def error(self, msg):
        """for error log"""
        msg = py2hlog.add_time_and_caller_file(self, msg)
        self._write_log("ERROR", msg)

    def warning(self, msg):
        """for warning log"""
        msg = py2hlog.add_time_and_caller_file(self, msg)
        self._write_log("WARNING", msg)

    def info(self, msg):
        """for info log"""
        msg = py2hlog.add_time_and_caller_file(self, msg)
        self._write_log("INFO", msg)

    def debug(self, msg):
        """for debug log"""
        msg = py2hlog.add_time_and_caller_file(self, msg)
        self._write_log("DEBUG", msg)

    def makehtml(self, output_file):
        """create html format of logs"""
        makehtml(self.file_name, output_file)


class makehtml():
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        makehtml.create_html_format(self)

    def create_html_format(self):
        """call makehtml class to create html form of simple text log file"""
        html_formater(self.input_file, self.output_file)
