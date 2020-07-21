from django.views.generic import ListView
from .models import Post


class BlogView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog.html"
    paginate_by = 5
