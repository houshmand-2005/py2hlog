import datetime
import inspect
import random
import string


class py2hlog():
    """main class -> here the functions we need called"""

    def __init__(self):
        self.file_name = None
        global caller
        caller = str(inspect.stack()[1][1])

    def __str__(self):
        return f"{self!r} in --> {self.file_name}"

    def _caller(self, msg, startline, endline):
        if startline != -1 and endline != -1:
            msg2 = py2hlog._ch_lines(self, startline, endline)
        else:
            msg2 = ""
        msg = py2hlog._add_time_and_caller_file(self, msg)
        msg += str(msg2)
        return msg

    def _ch_lines(self, startline, endline):
        with open(f'{caller}', 'r') as fp:
            # lines to read
            line_numbers_range = list(range(startline-1, endline))
            line_numbers = line_numbers_range
            # To store lines
            lines = []
            for i, line in enumerate(fp):
                if i in line_numbers:
                    lines.append(line.strip())
                elif i > int(line_numbers[-1:][0]):
                    # don't read after the last line to save time
                    break
        lines2 = ""
        lines3 = []
        for info in lines:
            info += " <br> "
            lines3 += info
        lines = lines2.join(lines3)

        def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
            return ''.join(random.choice(chars) for _ in range(size))
        count = "PY2HLOG"
        count += id_generator()
        addstyle = f"""
<br>
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#{count}">
See code
</button>

<div class="modal fade" id="{count}" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="staticBackdropLabel">Code : </h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        {lines}
      </div>
      <div class="modal-footer">
      </div>
    </div>
  </div>
</div>
"""
        return addstyle

    def _write_log(self, level, msg):
        """write log before transform to html"""
        path = self.file_name
        try:
            with open(path, "a") as log_file:
                log_file.write(f"[{level}] {msg}\n")
        except:
            print("Could not read The File")

    def _add_time_and_caller_file(self, msg):
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

    def critical(self, msg, startline=-1, endline=-1):
        """for critical log"""
        msg = self._caller(msg, startline, endline)
        self._write_log("CRITICAL", msg)

    def error(self, msg, startline=-1, endline=-1):
        """for error log"""
        msg = self._caller(msg, startline, endline)
        self._write_log("ERROR", msg)

    def warning(self, msg, startline=-1, endline=-1):
        """for warning log"""
        msg = self._caller(msg, startline, endline)
        self._write_log("WARNING", msg)

    def info(self, msg, startline=-1, endline=-1):
        """for info log"""
        msg = self._caller(msg, startline, endline)
        self._write_log("INFO", msg)

    def debug(self, msg, startline=-1, endline=-1):
        """for debug log"""
        msg = self._caller(msg, startline, endline)
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


class html_formater():
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        html_formater._normallaze_txt(self)

    def _normallaze_txt(self):
        try:
            with open(self.input_file, "r") as input_file:
                log_txt = input_file.read()
        except:
            print("Could not read The File")
        status_txt = ""
        normall_txt = ""
        for char in log_txt:
            if char == "[":
                status = True
                normall_txt += "|"
            elif char == "]":
                status = False
                status_txt += "|"
            elif status:
                status_txt += char
            else:
                normall_txt += char

        status_txt = (status_txt.split("|"))[0:-1]
        normall_txt = (normall_txt.split("|")[1:])
        html_formater._write_html(
            self, status_txt, normall_txt, self.output_file)

    def _write_html(self, status_txt, normall_txt, output_file):
        self.output_file = output_file
        self.status_txt = status_txt
        self.normall_txt = normall_txt
        basehtml = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>py2hlog</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
</head>
<body style="background-color: rgb(243, 243, 243);">
<div style="margin-left: 40px;margin-right: 700px;">
<h1>py2hlog</h1>
<br>
"""
        counter = 0
        status = {
            'CRITICAL': """<div class="alert alert-dark" role="alert">""",
            'ERROR': """<div class="alert alert-danger" role="alert">""",
            'WARNING': """<div class="alert alert-warning" role="alert">""",
            'INFO': """<div class="alert alert-info" role="alert">""",
            'DEBUG': """<div class="alert alert-success" role="alert">""",
        }
        for sent in self.normall_txt:
            sent = sent.replace('\n', "")
            for stat in status:
                if self.status_txt[counter] == stat:
                    status_style = status[stat]
            basehtml += f"""{status_style}{self.status_txt[counter]}</div>"""
            basehtml += f"""
<div class="card">
  <div class="card-body">
    {sent}
  </div>
</div>"""
            basehtml += "<hr>"
            counter += 1
        time = datetime.datetime.now()
        basehtml += f"""
<h4>last edit :{time.strftime("%Y-%m-%d %H:%M:%S")}</h4>
</div>
</body>
</html>
"""
        try:
            with open(self.output_file, "w") as output:
                output.write(basehtml)
        except:
            print("Could not read The File")
