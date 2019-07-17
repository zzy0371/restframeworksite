from django.conf.urls import url,include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'books',views.BookViewSet)
router.register(r'heros',views.HeroViewSet)
urlpatterns = [
    url(r'^',include(router.urls)),
]
