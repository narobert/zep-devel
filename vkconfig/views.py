from django.shortcuts import render, render_to_response
from django.http import JsonResponse
from django.conf import settings
import requests


def dashboard(request):

    return render_to_response('dashboard.html')


def search(request):

    query = request.POST.get('query', '')

    r = requests.get(settings.BASE_URL + 'api/tracklist/{}'.format(query))

    return JsonResponse({'tracklist': r.json()})