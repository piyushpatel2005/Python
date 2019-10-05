from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    context = {
        "title": "Home Page",
        "content": "Welcome to the home page."
    }
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "About Page",
        "content": "Welcome to the about page."
    }
    return render(request, "home_page.html", context)


def contact_page(request):
    context = {
        "title": "Contact Page",
        "content": "Welcome to the contact page."
    }
    return render(request, "home_page.html", context)


def home_page_old(request):

    html_ = """
    <!doctype html>
    <html lang="en">
      <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css">

        <title>Hello, world!</title>
      </head>
      <body>
      <div class="text-center">
        <h1>Hello, world!</h1>
      </div>

        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js""></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/js/bootstrap.min.js"></script>
      </body>
    </html>
    """
    return HttpResponse(html_)
