import datetime


class html_formater():
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        html_formater._normallaze_txt(self)

    def _normallaze_txt(self):
        with open(self.input_file, "r") as input_file:
            log_txt = input_file.read()
        # print(log_txt)
        staus_txt = ""
        normall_txt = ""
        for char in log_txt:
            if char == "[":
                staus = True
                normall_txt += "|"
            elif char == "]":
                staus = False
                staus_txt += "|"
            elif staus:
                staus_txt += char
            else:
                normall_txt += char

        staus_txt = (staus_txt.split("|"))[0:-1]
        normall_txt = (normall_txt.split("|")[1:])
        html_formater._write_html(
            self, staus_txt, normall_txt, self.output_file)

    def _write_html(self, staus_txt, normall_txt, output_file):
        self.output_file = output_file
        self.staus_txt = staus_txt
        self.normall_txt = normall_txt
        basehtml = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>py2hlog</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
</head>
<body style="background-color: rgb(243, 243, 243);">
<div style="margin-left: 40px;margin-right: 700px;">
<h1>py2hlog</h1>
<br>
"""
        counter = 0
        staus = {
            'CRITICAL': """<div class="alert alert-dark" role="alert">""",
            'ERROR': """<div class="alert alert-danger" role="alert">""",
            'WARNING': """<div class="alert alert-warning" role="alert">""",
            'INFO': """<div class="alert alert-info" role="alert">""",
            'DEBUG': """<div class="alert alert-success" role="alert">""",
        }
        for sent in self.normall_txt:
            sent = sent.replace('\n', "")
            for stat in staus:
                if self.staus_txt[counter] == stat:
                    status_style = staus[stat]
            basehtml += f"""{status_style}{self.staus_txt[counter]}</div>"""
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
        with open(self.output_file, "w") as output:
            output.write(basehtml)
