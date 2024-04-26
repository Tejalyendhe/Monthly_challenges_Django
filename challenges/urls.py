from django.urls import path
from . import views


urlpatterns = [
    path("january/",views.january),
    path("love/",views.love),
    path("django1/",views.django1),
]