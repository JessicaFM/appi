from django.shortcuts import render

from .models import AppiRequest


def index(request):
    all_requests = AppiRequest.objects.all()
    context = {
        'all_requests': all_requests,
    }
    return render(request, 'appi/index.html', context)