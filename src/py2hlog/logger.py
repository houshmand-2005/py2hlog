import pathlib
import datetime
import inspect
import random
import string
try:
    from . import html_files
    from . import addtree
except Exception:
    try:
        from src.py2hlog import html_files
        from src.py2hlog import addtree
    except Exception:
        from html_files import *
        from addtree import *
TREE_OUTPUT_SEND = ""


class py2hlog():
    """main class -> here the functions we need called"""

    def __init__(self):
        self.file_name = None
        global caller
        caller = str(inspect.stack()[1][1])

    def __str__(self):
        return f"{self!r} in --> {self.file_name}"

    TREE_PATH = 'tree_config.txt'

    def _caller(self, msg, startline, endline):
        if startline != -1 and endline != -1:
            msg2 = py2hlog._ch_lines(self, startline, endline)
        else:
            msg2 = ""
        msg = py2hlog._add_time_and_caller_file(self, msg)
        msg += str(msg2)
        return msg

    def _ch_lines(self, startline, endline):
        with open(f'{caller}', 'r', encoding="utf-8") as fp:
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
        addstyle = html_files.insert_status(count, lines)
        return addstyle

    def _write_log(self, level, msg):
        """write log before transform to html"""
        path = self.file_name
        try:
            with open(path, "a") as log_file:
                log_file.write(f"[{level}] {msg}\n")
        except Exception as ex:
            print(ex)
            print("Could not write into The File")

    def _add_address(self, inpaddress, inpfilename):
        if addtree.ALL_ADDRESS == {}:
            addtree.ALL_ADDRESS[addtree.COUNTER_ADDRESS] = [
                inpaddress, inpfilename]
            addtree.COUNTER_ADDRESS += 1
            return False
        for adders in addtree.ALL_ADDRESS:
            if addtree.ALL_ADDRESS[adders][0] == inpaddress and addtree.ALL_ADDRESS[adders][1] == inpfilename:
                return True
            addtree.ALL_ADDRESS[addtree.COUNTER_ADDRESS] = inpaddress, inpfilename
            addtree.COUNTER_ADDRESS += 1
            return False

    def _write_tree(self, tree_output):
        """write tree path to another file"""
        try:
            with open(py2hlog.TREE_PATH, "a", encoding="utf-8") as log_file:
                log_file.write(tree_output)
        except Exception as ex:
            print(ex)
            print("Could not read The File")

    def _add_time_and_caller_file(self, msg):
        """add time for each log status"""
        now = str(datetime.datetime.now())
        msg += html_files.insert_time_status(now)
        path12 = pathlib.Path(caller)
        filename = path12.name
        pathname = path12.parent
        add_addr = self._add_address(pathname, filename)
        if add_addr:
            pass
        else:
            tree_output = addtree.tree(
                pathlib.Path.home() / pathname, filename=filename)
            global TREE_OUTPUT_SEND
            TREE_OUTPUT_SEND += tree_output
            self._write_tree(TREE_OUTPUT_SEND)

        msg += html_files.insert_caller_status(caller)
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
        html_formatter(self.input_file, self.output_file)


class html_formatter():
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        html_formatter._normalized_txt(self)

    def _read_tree(self, filepath):
        """read the tree file and make it ready for html output"""
        TREE_OUTPUT_SEND = ""
        try:
            with open(filepath, "r", encoding="utf-8") as tree_input:
                TREE_OUTPUT_SEND = tree_input.read()
        except Exception:
            print("Could not read The File")
        return html_files.insert_tree(TREE_OUTPUT_SEND)

    def _normalized_txt(self):
        try:
            with open(self.input_file, "r", encoding="utf-8") as input_file:
                log_txt = input_file.read()
        except Exception:
            print("Could not read The File")
        status_txt = ""
        normal_txt = ""
        for char in log_txt:
            if char == "[":
                status = True
                normal_txt += "|"
            elif char == "]":
                status = False
                status_txt += "|"
            elif status:
                status_txt += char
            else:
                normal_txt += char

        status_txt = (status_txt.split("|"))[0:-1]
        normal_txt = (normal_txt.split("|")[1:])
        html_formatter._write_html(
            self, status_txt, normal_txt, self.output_file)

    def _write_html(self, status_txt, normal_txt, output_file):
        self.output_file = output_file
        self.status_txt = status_txt
        self.normal_txt = normal_txt
        basehtml = html_files.base_html_code()
        counter = 0
        status = {
            'CRITICAL': """<div class="alert alert-dark" role="alert">""",
            'ERROR': """<div class="alert alert-danger" role="alert">""",
            'WARNING': """<div class="alert alert-warning" role="alert">""",
            'INFO': """<div class="alert alert-info" role="alert">""",
            'DEBUG': """<div class="alert alert-success" role="alert">""",
        }
        for sent in self.normal_txt:
            sent = sent.replace('\n', "")
            for stat in status:
                if self.status_txt[counter] == stat:
                    status_style = status[stat]
            basehtml += f"""{status_style}{self.status_txt[counter]}</div>"""
            basehtml += html_files.insert_sent_base_code(sent)
            basehtml += "<hr>"
            counter += 1
        time = datetime.datetime.now()
        global TREE_OUTPUT_SEND
        basehtml += html_formatter._read_tree(self, py2hlog.TREE_PATH)
        basehtml += html_files.insert_last_edit_time(
            time.strftime("%Y-%m-%d %H:%M:%S"))
        try:
            with open(self.output_file, "w", encoding="utf-8") as output:
                output.write(basehtml)
        except Exception as ex:
            print(ex)
            print("Could not write into The File")
