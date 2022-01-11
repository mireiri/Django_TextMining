from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('download/<int:id>/', views.download, name='download'),
    path('delete/<int:id>/', views.delete, name='delete')
]
