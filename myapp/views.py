from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'myapp1/base.html') # Refer to the template path here
