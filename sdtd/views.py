from django.shortcuts import render, redirect
from django.http import HttpResponse


def sdtd(request):
	return render(request, 'sdtd/serverlist.html')

def whisperwind(request):
    return render(request, 'sdtd/whisperwind/whisperwindmain.html')

def wwrules(request):
    return render(request, 'sdtd/whisperwind/wwpages/rules.html')

def wwcommands(request):
    return render(request, 'sdtd/whisperwind/wwpages/commands.html')

def wwdonations(request):
    return render(request, 'sdtd/whisperwind/wwpages/donations.html')

def karazhan(request):
    return render(request, 'sdtd/karazhan/karazhanmain.html')

def kararules(request):
    return render(request, 'sdtd/karazhan/karapages/rules.html')

def karacommands(request):
    return render(request, 'sdtd/karazhan/karapages/commands.html')

def karadonations(request):
    return render(request, 'sdtd/karazhan/karapages/donations.html')
