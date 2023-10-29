from django.contrib import admin
from django.urls import path,include
from TaskHive import views

urlpatterns = [
    path('', views.homepage,name='home'),
    path('signup/', views.signup,name='signup'),
    path('mainpage/', views.mainpage,name='mainpage'),
    path('add-todo/',views.addtodo),
    path('logout/',views.user_logout),
    path('delete-task/<int:id>',views.delete_task),
    
]

    