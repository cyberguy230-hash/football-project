from django.urls import path
from . import views

urlpatterns = [
    path('', views.soccer, name="football"),
    path('submit/', views.submit, name="submit"),
    path('make-admin/', views.create_admin),
]