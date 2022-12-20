from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import api


def schema(request):
    print('schema')
    submitted = False
    if request.method == 'POST':
        schema_name = request.POST['schema_name']
        schema_version = request.POST['schema_version']
        schema_attrs = request.POST['schema_attrs']

        if api.create_schema(schema_name, schema_version, schema_attrs):
            return HttpResponseRedirect('/schema?submitted=True')
        else:
           return render(request, "metadata/schema.html", {'error': True})  
    else:
        if 'submitted' in request.GET:
            submitted = True 

    return render(request,'metadata/schema.html', {'submitted': submitted})


def get_schemas(request):
    print('get_schemas')

    schemas = api.get_schemas()

    return render(request, 'metadata/get-schemas.html', {'schemas': schemas})    


def get_schema_detail(request, schema_id):
    print('get_schema_detail')

    schema_detail = api.get_schema_by_id(schema_id)   
    
    return render(request, 'metadata/schema-detail.html', {'schema_id': schema_id, 'schema_detail': schema_detail})  
