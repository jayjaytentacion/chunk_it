from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.DashBoardView, name = "dashboard"),
    path("upload_file/", views.UploadFileView, name = "upload"),
    path("chunk_file/", views.ChunkFileView, name="chunk"),
]