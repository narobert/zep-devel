from django.conf.urls import url
from api import views as api_views

urlpatterns = [
    url(r'^tracklist/(?P<query>.+)/$', api_views.get_tracklist, name='get_tracklist'),
]