from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^zoos/$',ZooListView.as_view()),
    url(r'zoos/(?P<pk>\d+)/',ZooDetailView.as_view()),
]