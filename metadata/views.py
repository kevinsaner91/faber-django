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

def credential_definition(request):
    print('credential_definition')
    submitted = False
    if request.method == 'POST':
        schema_id = request.POST['schema_id']
        tag = request.POST['tag']
        support_revoc = True if request.POST.get('support_revoc') == 'on' else False
        if support_revoc:
            revoc_reg_size = int(request.POST['revoc_reg_size'])
        else:
            revoc_reg_size = 100


        if api.create_creddef(schema_id, tag, str(support_revoc).lower(), revoc_reg_size):
            return HttpResponseRedirect('/credential-definition?submitted=True')
        else:
           return render(request, "metadata/creddef.html", {'error': True})  
    else:
        if 'submitted' in request.GET:
            submitted = True 

    return render(request,'metadata/creddef.html', {'submitted': submitted})

def get_creddefs(request):
    print('get_creddefs')

    creddefs = api.get_creddefs()

    return render(request, 'metadata/get-creddefs.html', {'creddefs': creddefs})

def get_creddef_detail(request, creddef_id):
    print('get_creddef_detail')

    creddef_detail = api.get_creddef_by_id(creddef_id)   
    
    return render(request, 'metadata/creddef-detail.html', {'creddef_id': creddef_id, 'creddef_detail': creddef_detail})  

def revocation_registry(request):
    print('revocation_registry')
    submitted = False
    if request.method == 'POST':
        creddef_id = request.POST['creddef_id']
        revoc_reg_size = int(request.POST['revoc_reg_size'])


        if api.create_revoc_reg(creddef_id, revoc_reg_size):
            return HttpResponseRedirect('/revocation-registry?submitted=True')
        else:
           return render(request, "metadata/revocreg.html", {'error': True})  
    else:
        if 'submitted' in request.GET:
            submitted = True 

    return render(request,'metadata/revocreg.html', {'submitted': submitted})

def get_revocation_registry(request):
    print('get_revocation_registry')

    revoc_regs = api.get_revocation_registry()

    return render(request, 'metadata/get-revocreg.html', {'revoc_regs': revoc_regs})

def get_revocreg_detail(request, revocreg_id):
    print('get_revocreg_detail')

    revocreg_detail = api.get_revocreg_by_id(revocreg_id)   
    
    return render(request, 'metadata/revocreg-detail.html', {'revocreg_id': revocreg_id, 'revocreg_detail': revocreg_detail})  


