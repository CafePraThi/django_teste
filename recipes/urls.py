from django.urls import path
from django.http import HttpResponse
from recipes.views import home, sobre


def my_view(request):
    return HttpResponse("cel:123")


urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', my_view),
]
