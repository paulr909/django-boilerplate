from django.views.generic import ListView
from .models import Item


class AboutView(ListView):
    model = Item
    context_object_name = "items"
    template_name = "about.html"
    paginate_by = 5
