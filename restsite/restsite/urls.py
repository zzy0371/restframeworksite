"""restsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from booktest.views import *
from shoptest.views import *
from authtest.views import *
from routertest.views import *
from serializertest.views import *
from rest_framework import routers
router = routers.DefaultRouter()
router.register('books', BookViewSet)
router.register('heros', HeroViewSet)
router.register('goods', GoodViewSet)
router.register('carts', CartViewSet)
router.register('serializers',SerializerModelViewSet)
router.register('auths',AuthModelViewSet)
router.register('zoos',ZooViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    url('',include(router.urls)),
    url('',include('viewtest.urls')),
    # url('',include('routertest.urls')),
]

# 绑定之后才可以有授权登录功能
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
