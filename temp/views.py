from django.shortcuts import render, redirect
from .forms import TempForm
from .models import Temperature
from django.contrib import messages
from dateutil.relativedelta import relativedelta
from datetime import date

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
    # last_3_mths = date.today() + relativedelta(months=-3)
    temperature_record = Temperature.objects.all().order_by('-date_recorded')
    # temperature_record = Temperature.objects.filter(date_recorded=last_3_mths)
    return render(request, 'temp/chart.html', {'temperature_record': temperature_record})
