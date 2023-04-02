from django.urls import path

from . import views

urlpatterns = [
    path("popular-frameworks/", views.AboutView.as_view(), name="popular-frameworks"),
    path("cars/", views.upload_car, name="cars"),
    path("collection/", views.CarCollectionView.as_view(), name="collection"),
    path("delete/<int:pk>", views.delete_image, name="delete-image"),
]
