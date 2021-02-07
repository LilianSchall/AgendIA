from django.shortcuts import render
from .models import Task
from .qr_code import get_data
from datetime import date

def index(request):
    tasks = Task.objects.filter(beginning__gt=date.today())
    data = {}
    #print(get_data())
    for t in tasks:
        if t.beginning.month in data.keys():
            data[t.beginning.month][t.beginning.day] = t.title
        else:
            data[t.beginning.month] = {t.beginning.day: t.title}
    print(data)
    return render(request, 'myPWA/index.html', locals())

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        beginning = request.POST.get("beginning")
        ending = request.POST.get("ending")
        new_task = Task.objects.create(title=title,
                                       beginning=beginning,
                                       ending=ending)
        new_task.save()
