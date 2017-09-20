from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

#here we're  passing variables from Python to our HTML templates. 
def contact(request):
    return render(request, 'personal/basic.html',{'content':['If you would like to contact me, you can email me.','ciyaelcicek@gmail.com']})

