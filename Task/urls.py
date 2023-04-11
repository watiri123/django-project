from django.urls import path
from .import views


urlpatterns = [
   path("", views.Task, name="task"),
   path("add/", views.add, name="add")
]