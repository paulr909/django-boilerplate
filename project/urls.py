from django.urls import path, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

sitemaps = {"static": StaticViewSitemap}

urlpatterns = [
    path("", include("home.urls")),
    path("", include("about.urls")),
    path("", include("blog.urls")),
    path("", include("contact.urls")),
    path(
        "sitemap.xml/",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("admin/", admin.site.urls),
]
