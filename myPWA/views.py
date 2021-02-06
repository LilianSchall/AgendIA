from django.shortcuts import render
from .models import Task
from .qr_code import get_data

def index(request):
    tasks = Task.objects.all()
    data = {}
    print(get_data())
    for t in tasks:
        if t.beginning.month in data.keys():
            data[t.beginning.month][t.beginning.day] = t.title
        else:
            data[t.beginning.month] = {t.beginning.day: t.title}
    return render(request, 'myPWA/index.html', locals())