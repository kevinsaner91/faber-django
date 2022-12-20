from django.shortcuts import render
from django.http import HttpResponseRedirect
from .api import api

def connections(request):
    print('Connections')
    ConnectionsObject = api()
    active_connections = ConnectionsObject.get_active_connections()

    return render(request,'connections/connections.html', {'active_connections': active_connections})


def new_connection(request):
    print("New Connection")
    ConnectionsObject = api()
    connection_invitation = ConnectionsObject.get_connection_invitation()

    return render(request, 'connections/new_connection.html', {'connection_invitation': connection_invitation})

def accept_connection(request):
    print("Accept Connection")
    submitted = False
    if request.method == 'POST':
        connection_info = request.POST['connection_info']
        
        ConnectionsObject = api()
        if ConnectionsObject.accept_connection(connection_info):
            return HttpResponseRedirect('/accept?submitted=True')
        else:
           return render(request, "connections/accept.html", {'error': True})  
    else:
        if 'submitted' in request.GET:
            submitted = True    

    return render(request, "connections/accept.html", {'submitted': submitted})    
             


