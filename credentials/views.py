from django.shortcuts import render
from metadata import api

def issue_credential(request):

    schema_list = api.get_schemas()

    

    return render(request, 'credentials/issue-credential.html', {'schema_list':schema_list})  
