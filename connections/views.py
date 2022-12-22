from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import api

def connections(request):
    print('Connections')

    active_connections = api.get_active_connections()

    return render(request,'connections/connections.html', {'active_connections': active_connections})


def new_connection(request):
    print("New Connection")

    connection_invitation = api.get_connection_invitation()

    return render(request, 'connections/new_connection.html', {'connection_invitation': connection_invitation})

def accept_connection(request):
    print("Accept Connection")
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
             


