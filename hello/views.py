import re
from django.utils.timezone import datetime
#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from hello.forms import LogMessageForm
from hello.models import LogMessage
from django.views import generic

# Create your views here.
def home(request):
    return render(request, "hello/home.html")

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "hello/log_message.html", {"form": form})
    
class MessageListView(generic.ListView):
    model = LogMessage

def home_bak(request):
    return(HttpResponse("Hello, Django!"))

def hello_there(request, name):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def hello_there_backup(request, name):
    print('http://127.0.0.1:8000/hello/Rafa')
    now = datetime.now()
    formated_now = now.strftime("%d de %B de %Y às %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-z][A-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello, there, " + clean_name + "! It's" + formated_now
    return HttpResponse(content)
    