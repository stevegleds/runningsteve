from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     latest_runner_list = Runner.objects.order_by('first_name')[:5]
#     context = {'latest_runner_list': latest_runner_list}
#     return render(request, 'running/index.html', context)


def index(request):
    return render(request, 'runningsteve/index.html')
