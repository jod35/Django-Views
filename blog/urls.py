from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    path('',views.MyView.as_view(),name='home'),
    path('users/',views.listing,name='users'),
    path('delete/<int:id>/',views.delete,name='delete_user'),
    path('update/<pk>',views.UserUpdateView.as_view(),name='update')
]