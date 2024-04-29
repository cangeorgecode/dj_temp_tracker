from django.shortcuts import render, redirect
from .forms import TempForm
from .models import Temperature
from django.contrib import messages

def index(request):
    form = TempForm
    temperature = Temperature.objects.all()
    context = {
        'form': form,
        'temperature': temperature,
    }
    if request.method == "POST":
        form = TempForm(request.POST)
        form.save()
        messages.success(request, 'Temperature added')
        return redirect('index')
    return render(request, 'temp/index.html', context)

def chart(request):
    temperature = Temperature.objects.all()
    return render(request, 'temp/chart.html', {'temperature': temperature})
