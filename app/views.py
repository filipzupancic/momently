from django.shortcuts import render

# Create your views here.


def sample_function(request):

    return render(request, 'example.html')