import requests
import json
import string


def create_schema(name, version, attrs):
    print('create_schema')

    attrs = attrs.split(",")
    json_array = json.dumps(attrs)
    attr_data = json.loads(json_array)

    url = 'https://faber-api.educa.ch/schemas'
    data = {
        "attributes": attr_data,
        "schema_name": name,
        "schema_version": version
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


def get_schemas():
    print('get_schemas')

    url = 'https://faber-api.educa.ch/schemas/created'

    response = requests.get(url, 'GET')
    data = json.loads(response.text)

    schema_list = list()

    for schema_id in data["schema_ids"]:
            schema_list.append(
                {
                    "schema_id":schema_id
                }
            )
                
    return schema_list


def get_schema_by_id(schema_id):
    print('get_schema_by_id')

    url = 'https://faber-api.educa.ch/schemas/' + schema_id    

    response = requests.get(url, 'GET')
    data = json.loads(response.text)

    return data

def create_creddef(schema_id, tag, support_revoc, revoc_reg_size):
    print('create_creddef')

    url = 'https://faber-api.educa.ch/credential-definitions'
    data = {
        "revocation_registry_size": revoc_reg_size,
        "schema_id": schema_id,
        "support_revocation": support_revoc,
        "tag": tag
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

def get_creddefs():
    print('get_creddefs')

    url = 'https://faber-api.educa.ch/credential-definitions/created'

    response = requests.get(url, 'GET')
    data = json.loads(response.text)

    creddef_list = list()

    for creddef_id in data["credential_definition_ids"]:
            creddef_list.append(
                {
                    "creddef_id":creddef_id
                }
            )
                
    return creddef_list

def get_creddef_by_id(creddef_id):
    print('get_creddef_by_id')

    url = 'https://faber-api.educa.ch/credential-definitions/' + creddef_id    

    response = requests.get(url, 'GET')
    data = json.loads(response.text)

    return data
