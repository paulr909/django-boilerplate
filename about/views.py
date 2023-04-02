from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .forms import CarForm
from .models import Item, CarCollection


class AboutView(ListView):
    model = Item
    context_object_name = "items"
    template_name = "about.html"
    paginate_by = 5


class CarCollectionView(ListView):
    model = CarCollection
    context_object_name = "items"
    template_name = "collection.html"
    paginate_by = 3


def upload_car(request):
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, "Car uploaded, Thank you!")
            form.save()
        else:
            context = {"form": form}
            return render(request, "car.html", context)
    context = {"form": CarForm()}
    return render(request, "car.html", context)


def delete_image(request, pk):
    car = get_object_or_404(CarCollection, pk=pk)
    car.delete()
    return redirect("collection")
