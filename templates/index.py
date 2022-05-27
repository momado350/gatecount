<!DOCTYPE html>
<html lang="en">

<head>
   <meta charset="UTF-8">
   <title>MobileNet SSD Detector</title>
   <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css"
      integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
   <link rel="stylesheet" href="{{ url_for('static', filename='css/index.css') }}">

</head>

<body>
   {% with messages = get_flashed_messages() %}
   {% if messages %}
   <ul class=flashes>
      {% for message in messages %}
      <li>{{ message }}</li>
      {% endfor %}
   </ul>
   {% endif %}
   {% endwith %}
   <nav class="navbar navbar-dark bg-dark ">
      <a class="navbar-brand navbar-center" href="#">MobileNet SSD Demo</a>
   </nav>