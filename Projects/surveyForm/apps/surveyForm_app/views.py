from django.shortcuts import render, redirect

# Create your views here.
def index(request): # form is here
    # ADD COUNTER
    if "counter" in request.session: # if counter exists, do nothing
        pass
    else: # create counter key in session and set to 0
        request.session['counter'] = 0
    return render(request, "surveyForm_app/index.html")

def surveyProcess(request): # post/form data gets sent to this route
    # increment counter
    request.session['counter'] += 1
    info = { #packaging data in dictionary.
        "name": request.POST['Name'],
        "dojoLoc": request.POST['dojoLoc'],
        "favLang": request.POST['favLang'],
        "comments": request.POST['comments']
        }
    request.session['info'] = info # storing data in session
    return redirect("/result") # redirecting to result template

def surveyResult(request):
    return render(request, "surveyForm_app/result.html")

def sessionClear(request): # clear the session.
    request.session.flush()
    return redirect("/")
