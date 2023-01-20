import requests
import json
from metadata import api as metadata_api


def get_credential_def_from_schema_id(schema_id):
    print('get_credential_def_from_schema_id')
    url = 'https://faber-api.educa.ch/credential-definitions/created?schema_id=' + schema_id

    response = requests.get(url, 'GET')
    data = json.loads(response.text)

    creddef_list = list()

    for credential_definition_id in data["credential_definition_ids"]:
        creddef_list.append(
            {
                "creddef_id": credential_definition_id,
            }
        )

    return creddef_list

def get_attribute_list_from_schema_id(schema_id):
    print('get_attribute_list_from_schema_id')
    data = metadata_api.get_schema_by_id(schema_id)

    schema = data['schema']
    attributes = schema['attrNames']

    attributes_list = list()

    for attribute in attributes:
        attributes_list.append(
            {
                'key':attribute
            }
        )

    return attributes_list    

def issue_credential(connection_id, creddef_id, attributes):
    print('issue_credential')
    url = 'https://faber-api.educa.ch/issue-credential-2.0/send-offer'

    data = {   
        "connection_id": connection_id, 
        "comment": "Credential offer", 
        "auto_remove": "false", 
        "credential_preview": {
            "@type": "https://didcomm.org/issue-credential/2.0/credential-preview", 
            "attributes": attributes
        },
        "filter": {
            "indy": {
                "cred_def_id": creddef_id
            }
        },
        "trace": "true"
    }
    headers = {"Content-Type": "application/json"}


    response = requests.post(
        url,
        json=data,
        headers=headers)

    print(data)

    if response.status_code == 200:
        print('successful')
        return True
    else:
        return False 

def get_rev_regs():
    print('get_rev_regs')

    url = 'https://faber-api.educa.ch/revocation/registries/created'

    response = requests.get(url, 'GET')
    data = json.loads(response.text)

    rev_reg_list = list()

    for rev_reg_id in data['rev_reg_ids']:
        rev_reg_list.append(
            rev_reg_id
        )
    return rev_reg_list   

def get_credential_from_rev_reg(rev_reg_id):
    print('get_credential_from_rev_reg')

    url = 'https://faber-api.educa.ch/revocation/registry/' + rev_reg_id +'/issued/details'
    response = requests.get(url, 'GET')
    data = json.loads(response.text)

    credentials = list()

    for credential in data:
        credentials.append(
            {
                'cred_ex_id': credential['cred_ex_id'],
                'state': credential['state'],
                'updated_at': credential['updated_at'],
            }
        )
    return credentials   


def get_revocation_status(cred_ex_id):
    print('get_revocation_status')

    url = 'https://faber-api.educa.ch/revocation/credential-record?cred_ex_id=' + cred_ex_id
    response = requests.get(url, 'GET')
    data = json.loads(response.text)

    print(data['result'])

    credential = data['result']

    return credential   

def revoke_credential(cred_ex_id , rev_reg_id, cred_rev_id):
    print('revoke_credential')

    url = 'https://faber-api.educa.ch/revocation/revoke'

    data = {
        "rev_reg_id": rev_reg_id,
        "cred_rev_id": cred_rev_id,
        "publish": "true",
        "notify": False,
        "comment": "You cheated ...",
    }       
    headers = {"Content-Type": "application/json"}

    print(data)

    response = requests.post(
        url,
        json=data,
        headers=headers)

    if response.status_code == 200:
        print('revocation successful')
        #response = requests.delete('https://faber-api.educa.ch/issue-credential-2.0/records/' + cred_ex_id)
        return True
    else:
        return False




