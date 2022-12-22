from django.urls import path, re_path
from . import views

urlpatterns = [
    path('issue-credential', views.select_schema, name='issue-credential'),
    path('issue-credential-detail/<str:schema_id>', views.issue_credential_detail, name='issue-credential-detail')
]