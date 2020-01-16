import requests
from django.http import HttpResponse, JsonResponse

from cachecontrol import CacheControl
from cachecontrol.heuristics import ExpiresAfter
from cachecontrol_django import DjangoCache


cached_sess = CacheControl(
    requests.session(),
    cache=DjangoCache(),
    heuristic=ExpiresAfter(days=15)
)


def variomes_single_ref(request):
    # proxy requests to variomes server
    response = cached_sess.get('http://candy.hesge.ch/Variomes3/api/fetchLit.jsp', params=request.GET)

    if response.status_code != 200:
        return HttpResponse(response.content, status=response.status_code)

    return JsonResponse(response.json())


def variomes_search(request):
    # proxy requests to variomes server
    response = cached_sess.get('http://candy.hesge.ch/Variomes3/api/rankLit.jsp', params=request.GET)

    if response.status_code != 200:
        return HttpResponse(response.content, status=response.status_code)

    return JsonResponse(response.json())
