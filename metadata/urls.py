from django.urls import path, re_path
from . import views

urlpatterns = [
    path('schema', views.schema, name='create-schema'),
]