from django.shortcuts import render, redirect
from .models import WasHere #The dot before models means current directory or
#current application. Both views.py and models.py are in the same directory.
#This means we can use . and the name of the file (without .py). Then we import the name of the model (WasHere).
from django.utils import timezone
from .forms import NameForm


def here_list(request):
    people = WasHere.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #Orders and publishs who was there. We will pass "people" to the template.
    return render(request, 'i_was_here/here_list.html', {'people': people})

def post_new(request):
    if request.method == "POST": #The result of request.method == "POST" is a boolean value - True if the current request from a user was performed using the HTTP "POST" method, of False otherwise
        form = NameForm(request.POST) # request.POST adds "this field is required" statement and does not accept an empy fied.
        if form.is_valid(): #checks if everything okay is, for example if all the required fields are filled.
            post = form.save(commit=False) #says "wait to save the form"
            post.published_date = timezone.now()
            post.save()
            return redirect('here_list') # "here_list" is name of a urlpattern. See urls.py.
    else:
        form = NameForm()
    return render(request, 'i_was_here/post_edit.html', {'form': form})
