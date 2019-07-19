from django.conf.urls import url
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    url(r'^viewmodellist/$',viewmodelslist),
    url(r'^viewmodellist/(\d+)/$',viewmodeldetail),
    url(r'^cviewmodellist/$', ViewModelListView.as_view()),
    url(r'^cviewmodellist/(\d+)/$', ViewModelDetailView.as_view()),
    url(r'^cmviewmodellist/$', ViewModelListMixinView.as_view()),
    url(r'^cmviewmodellist/(?P<pk>\d+)/$', ViewModelDetailMixinView.as_view()),
]

# 添加后缀  注意视图函数需要format=None
urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)