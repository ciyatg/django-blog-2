from django.shortcuts import render

def here_list(request):
    return render(request, 'i_was_here/here_list.html', {})
