from django.urls import path

from . import views

urlpatterns = [path("popular-frameworks/", views.AboutView.as_view(), name="popular-frameworks")]
