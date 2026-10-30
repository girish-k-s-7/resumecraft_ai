from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),

    path("builder/", views.builder_page, name="builder"),

    path("analyzer/", views.analyzer_page, name="analyzer"),
]
