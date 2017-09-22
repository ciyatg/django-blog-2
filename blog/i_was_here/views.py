from django.shortcuts import render
from .models import WasHere #The dot before models means current directory or
#current application. Both views.py and models.py are in the same directory.
#This means we can use . and the name of the file (without .py). Then we import the name of the model (WasHere).
from django.utils import timezone
from .forms import NameForm


def here_list(request):
    people = WasHere.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #Orders and publishs who was there. We will pass "people" to the template.
    return render(request, 'i_was_here/here_list.html', {'people': people})

def post_new(request):
    form = NameForm()
    return render(request, 'i_was_here/post_edit.html', {'form': form})
