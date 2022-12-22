from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from metadata import api as metadata_api
from connections import api as connections_api
from . import api

def select_schema(request):
    schema_list = metadata_api.get_schemas()
    
    if request.method == 'POST':
        schema_id = request.POST['schema_id']
                
        return redirect('/issue-credential-detail/' + schema_id)
           

    return render(request, 'credentials/issue-credential.html', {'schema_list':schema_list})


def issue_credential_detail(request, schema_id):
        creddef_list = api.get_credential_def_from_schema_id(schema_id)
        connections_list = connections_api.get_active_connections()
        attributes_list = api.get_attribute_list_from_schema_id(schema_id)

        return render(request, 'credentials/issue-credential-detail.html', {'creddef_list': creddef_list, 'connections_list': connections_list, 'attributes_list': attributes_list})

def issue_credential(request):
    print('issue_credential')
    submitted = False
    if request.method == 'POST':
        connection_info = request.POST['connection_info']
        
        if api.accept_connection(connection_info):
            return HttpResponseRedirect('/accept?submitted=True')
        else:
           return render(request, "connections/accept.html", {'error': True})  
    else:
        if 'submitted' in request.GET:
            submitted = True    

    return render(request, "connections/accept.html", {'submitted': submitted})   






