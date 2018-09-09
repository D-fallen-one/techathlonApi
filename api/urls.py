from . import views
from django.urls import path

urlpatterns = [
    path('', views.default, name = 'default'),
    path('<str:to>/<str:frm>', views.defaultWithParams, name='defaultWithParams'),
    path('top10/', views.top10,name = 'top10'),
    path('edit/<str:isbn>/<int:rating>', views.editRating, name = 'editRating'),
    path('ubr/<str:user>/', views.userBasedRecommandation, name = 'userBasedRecommandation'),
    path('ibr/<str:isbn>/', views.itemBasedRecommandation, name = 'itemBasedRecommandation'),
    path('login/<str:user>/<str:password>/', views.login, name = 'login'),
    path('createUser/<str:user>/<str:password>/<str:email>/', views.createUser, name = 'createUser'),
    path('books/details/<str:isbn>/', views.bookdetails, name = 'bookdetails'),
]