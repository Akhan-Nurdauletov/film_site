from django.urls import path

from . import views

urlpatterns = [
    path('', views.MoviewsView.as_view())
]