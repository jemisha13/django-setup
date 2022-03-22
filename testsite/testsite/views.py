from django.shortcuts import render
from datetime import datetime
from . import test_model

def product(request):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    user = request.GET['pname']
    result = test_model.fake_model(int(user))
    return render(request, 'form.html', {'home': result,'current_time':current_time})


def home(request):
    return render(request, 'home.html')



