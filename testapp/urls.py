from django.conf.urls import url
from . import views
from .views import *



urlpatterns = [
    url('addpro/', views.saveimg, name='addpro'),
    url('success', success, name = 'success'),
]
    