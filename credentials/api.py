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
        "trace": "false"
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

def get_cred_ex_records():
    print('get_cred_ex_records')

    url = 'https://faber-api.educa.ch/issue-credential-2.0/records'

    response = requests.get(url, 'GET')
    data = json.loads(response.text)

    cred_ex_list = list()

    for cred_ex_record in data["results"]:
        indy = cred_ex_record['indy']
        cred_ex_list.append(
            {
                'cred_ex_id':indy['cred_ex_id'],
                'rev_reg_id':indy['rev_reg_id'],
                'cred_rev_id':indy['cred_rev_id'],
            }
        )
    return cred_ex_list    


def revoke_credential(cred_ex_id ,connection_id, rev_reg_id, cred_rev_id):
    print('revoke_credential')

    url = 'https://faber-api.educa.ch/revocation/revoke'

    data = {
        "rev_reg_id": rev_reg_id,
        "cred_rev_id": cred_rev_id,
        "publish": "true",
        "connection_id": connection_id,
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
        response = requests.delete('https://faber-api.educa.ch/issue-credential-2.0/records/' + cred_ex_id)
        if response.status_code == 200:
            return True
    else:
        return False




