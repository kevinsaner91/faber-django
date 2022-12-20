from django.shortcuts import render
from django.http import HttpResponseRedirect


def schema(request):
    return render(request,'metadata/schema.html', {'submitted': True})
