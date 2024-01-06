from django.shortcuts import render

# Create your views here.
def landing(request, *args, **kwargs):
    context = {

    }
    return render(request, 'landing.html', context)