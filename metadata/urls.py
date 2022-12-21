from django.urls import path, re_path
from . import views

urlpatterns = [
    path('schema', views.schema, name='create-schema'),
    path('get-schemas', views.get_schemas, name='get-schemas'),
    path('schema/<str:schema_id>/', views.get_schema_detail, name='get-schema-details'),
    path('credential-definition', views.credential_definition, name='create-credential-definition'),
    path('get-credential-definitions', views.get_creddefs, name='get-credential-definitions'),
    path('credential-definition/<str:creddef_id>/', views.get_creddef_detail, name='get-creddef-details'),
    path('revocation-registry', views.revocation_registry, name='revocation-registry'),
    path('get-revocation-registry', views.get_revocation_registry, name='get-revocation-registry'),
    path('revocation-registry/<str:revocreg_id>/', views.get_revocreg_detail, name='get-revocreg-details')
]