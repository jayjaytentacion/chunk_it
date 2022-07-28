from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.DashBoardView, name = "dashboard"),
    path("chunking/", views.ChunkView, name="chunk")
]