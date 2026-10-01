
from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("history/", views.history_page, name="history"),
    path("upload/", views.upload_csv, name="upload"),
]