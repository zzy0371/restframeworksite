from django.conf.urls import url
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    url(r'^viewmodellist/$',viewmodelslist),
    url(r'^viewmodellist/(\d+)/$',viewmodeldetail),
]

# 添加后缀  注意视图函数需要format=None
urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)