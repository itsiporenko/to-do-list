from django.urls import path

from  . import views

urlpatterns = [

    path('', views.index, name=""),

    path('edit_task/<str:pk>/', views.editTask, name="edit_task"),

]