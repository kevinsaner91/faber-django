from django.urls import path, re_path
from . import views

urlpatterns = [
    path('issue-credential', views.issue_credential, name='create-schema'),
]