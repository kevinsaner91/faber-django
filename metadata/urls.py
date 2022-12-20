from django.urls import path, re_path
from . import views

urlpatterns = [
    path('schema', views.schema, name='create-schema'),
    path('get-schemas', views.get_schemas, name='get-schemas'),
    path('schema/<str:schema_id>/', views.get_schema_detail, name='get-schema-details')
]