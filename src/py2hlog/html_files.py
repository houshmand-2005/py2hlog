def base_html_code():
    """base html file like title and import the bootstrap"""
    base_html_code_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <title>py2hlog</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
</head>
<body style="background-color: rgb(243, 243, 243);">
<div class="row">
<div class="col-7">
<div style="margin-left: 30px;margin-right: 50px;">
<h1>py2hlog</h1>
<br>"""
    return base_html_code_html


def insert_status(count, lines):
    """Html classes for insert a status like 'INFO'"""
    insert_status_html = f"""<br>
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
</div>"""
    return insert_status_html


def insert_time_status(datatime):
    """Html classes for insert time to status like 'INFO'"""
    insert_time_status_html = "<br><br><button type='button' class='btn btn-light' disabled> " + \
        datatime + " </button>"
    return insert_time_status_html


def insert_caller_status(caller):
    """Html classes for insert caller(which file insert the status)to status"""
    insert_caller_status_html = f"""<br><br>
<div class='dropdown'>
  <a class='btn btn-secondary dropdown-toggle' href='#' role='button' data-bs-toggle='dropdown' aria-expanded='false'>From this File</a>
  <ul class='dropdown-menu'>
    <li class='dropdown-item'>{caller}</li>
  </ul>
</div>"""
    return insert_caller_status_html


def insert_sent_base_code(sent):
    """Add final html to base file"""
    insert_sent_base_code_html = f"""<div class="card">
  <div class="card-body">
    {sent}
  </div>
</div>"""
    return insert_sent_base_code_html


def insert_tree(msg):
    """insert The contents of the executable file folder in html file"""
    insert_tree_html = '</div></div><br>' + \
        f"""
<div class="col-4" style="margin-top: 10px;font-family:monospace">
<div class="card text-bg-light mb-3" style="max-width: 20rem;">
  <div class="card-header">The contents of the executable file folder</div>
  <div class="card-body">
    <p class="card-text">{msg}</p>
  </div>
</div>
</div>"""
    return insert_tree_html


def insert_last_edit_time(time):
    """insert the last time anyone edit it"""
    insert_last_edit_time_html = f"""<h4 style="margin-left: 10px>last edit :{time}</h4>
    </div>
  </div>
</body>
</html>"""
    return insert_last_edit_time_html
