from . import views
from django.urls import path

urlpatterns = [
    path('',views.default, name = 'default'),
    path('<str:to>/<str:frm>',views.defaultWithParams, name='defaultWithParams'),
]