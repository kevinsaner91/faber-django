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
    print('issue_credential_detail')
    creddef_list = api.get_credential_def_from_schema_id(schema_id)
    connections_list = connections_api.get_active_connections()
    attributes_list = api.get_attribute_list_from_schema_id(schema_id)
   
    
    submitted = False
    if request.method == 'POST':
        attrs_list = list()

        values = request.POST
        for key, value in values.items():
            if key == 'connection_id':
                connection_id = value
            elif key == 'creddef_id':
                creddef_id = value
            elif key == 'csrfmiddlewaretoken':
                print(value)
            else:
                attrs_list.append(
                    {
                        'name':key,
                        'value':value
                    }
                )

        if api.issue_credential(connection_id, creddef_id, attrs_list):
            return HttpResponseRedirect('/issue-credential?submitted=True')
        else:
           return render(request, "credentials/issue-credential-detail.html", {'error': True}) 
    else:
        if 'submitted' in request.GET:
            submitted = True 

    return render(request, 'credentials/issue-credential-detail.html', {'submitted': submitted, 'creddef_list': creddef_list, 'connections_list': connections_list, 'attributes_list': attributes_list}) 

def get_rev_regs(request):
    print('credential_exchange_records')

    if request.method == 'POST':
        rev_reg_id = request.POST['rev_reg_id']

        return redirect('/issued-credentials-details/' + rev_reg_id)
    else:
        rev_regs = api.get_rev_regs()
        print(rev_regs)

        return render(request,'credentials/issued-credentials.html', {'rev_reg_list': rev_regs})   

def get_issued_creds_by_rev_reg(request, rev_reg_id):
    print('get_issued_creds_by_rev_reg')

    credentials = api.get_credential_from_rev_reg(rev_reg_id)

    print(credentials)

    return render(request,'credentials/issued-credentials-details.html', {'credentials': credentials})  





def revoke_credential(request, cred_ex_id, rev_reg_id, cred_rev_id):
    print('revoke_credential')
    submitted = False
    connections_list = connections_api.get_active_connections()

    if request.method == 'POST':
        connection_id = request.POST['connection_id']

        if api.revoke_credential(cred_ex_id, connection_id, rev_reg_id, cred_rev_id):
           return HttpResponseRedirect('/revoke-credential/' + cred_ex_id + '/'+ rev_reg_id + '/' + cred_rev_id +'?submitted=True') 
        else:
           return render(request, "credentials/revoke-credential.html", {'error': True})        
    else:
        if 'submitted' in request.GET:
            submitted = True        

    return render(request, 'credentials/revoke-credential.html', {'submitted': submitted, 'connections_list': connections_list, 'rev_reg_id': rev_reg_id, 'cred_rev_id':cred_rev_id})






