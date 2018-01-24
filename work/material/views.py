from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime
# from material.forms import NewUserForm

from django.shortcuts import render
from django.http import HttpResponseRedirect
# import MySQLdb
from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            name = form.cleaned_data['chat']
            print( name )
            return render(request, 'hey.html', {'form': form,'chat':name})
            # return HttpResponsek('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'hey.html', {'form': form})

