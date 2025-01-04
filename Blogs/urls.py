from django.urls import path
from . import views
urlpatterns = [
    path("blogDetails/<int:id>/", views.blog, name="blog")
]
