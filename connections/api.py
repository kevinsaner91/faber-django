import requests
import json
import base64



def get_active_connections():
    print('get_active_connections')
    response = requests.get(
         'https://faber-api.educa.ch/connections', 'GET')
    data = json.loads(response.text)

    connection_list = list()

    for records in data["results"]:
        if records["state"] == "active":
            connection_list.append(
                {
                    "connection_id": records["connection_id"],
                    "their_label": records["their_label"],
                    "their_did": records["their_did"],
                    "last_updated": records["updated_at"]
                }
            )

    return connection_list


def get_connection_invitation():
    print('new_connection_invitation')

    url = 'https://faber-api.educa.ch/out-of-band/create-invitation'
    data = {
          "accept": [
               "didcomm/aip1",
                "didcomm/aip2;env=rfc19"
               ],
           "alias": "",
          "handshake_protocols": [
                "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/didexchange/1.0"
               ],
           "metadata": {},
          "my_label": "Invitation to Alice",
            "protocol_version": "1.1",
            "use_public_did": "false"
          }
    headers = {"Content-Type": "application/json"}

    response = requests.post(
            url,
            json=data,
            headers=headers)

    print(response.json())

    data = json.loads(response.text)

    print(data)

    return data["invitation_url"]


def accept_connection(connection_info):
    print('accept_connection')
    base64_info = connection_info.split('=', 1)

    decoded_connection_bytes = base64.b64decode(base64_info[1])
    decoded_connection_info = decoded_connection_bytes.decode()

    url = 'https://faber-api.educa.ch/out-of-band/receive-invitation'
    data = decoded_connection_info
    headers = {"Content-Type": "application/json"}

    response = requests.post(
        url,
        json=data,
        headers=headers)

    if response.status_code == 200:
        print('successful')
        return True
    else:
        return False
