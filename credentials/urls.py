from django.urls import path, re_path
from . import views

urlpatterns = [
    path('issue-credential', views.select_schema, name='issue-credential'),
    path('issue-credential-detail/<str:schema_id>', views.issue_credential_detail, name='issue-credential-detail'),
    path('credentials', views.credential_exchange_records, name='revoke-credential'),
    path('revoke-credential/<str:cred_ex_id>/<str:rev_reg_id>/<str:cred_rev_id>', views.revoke_credential, name='revoke-credential'),
    path('revoke-credential', views.revoke_credential, name='revoke-credential')
]