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
    print(attributes_list)

    return attributes_list    




