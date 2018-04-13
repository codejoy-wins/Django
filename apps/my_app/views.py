from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    print request
    return HttpResponse("placeholder to display all the list of blogs")

def new(request):
    print "display new"
    return HttpResponse("placeholder to later display a new form to create a new blog")

def create(request):
    print "create"
    return redirect('/')

def show(request, number):
    print number
    return HttpResponse("placeholder to display blog " + number)

def edit(request, number):
    print number
    return HttpResponse("placeholder to edit blog " + number)

def destroy(request, number):
    print number
    return redirect('/')


def hello(request):
    print "Hey check it"
    something = {
        "hmm" : "Does this work?"
    }
    return render(request, 'my_app/index.html', something)

def odell(request):
    print "catches everything"
    return HttpResponse("Touchdown!  Odell Beckham Jr. catches everything")