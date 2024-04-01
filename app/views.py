from django.shortcuts import render
from .models import MyModel

def index(request):

    objs = MyModel.objects.all()
    context = {
        'objs': objs
    }
    return render(request, 'index.html',context)
