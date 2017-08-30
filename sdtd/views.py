from django.shortcuts import render, redirect
from django.http import HttpResponse


def sdtd(request):
	return render(request, 'sdtd/serverlist.html')





def screenshots(request):
	return render(request, 'sdtd/screenshots/screenshots.html')





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





def lightbringer(request):
    return render(request, 'sdtd/lightbringer/lightbringermain.html')

def lbinstall(request):
    return render(request, 'sdtd/lightbringer/lbpages/install.html')

def lbrules(request):
    return render(request, 'sdtd/lightbringer/lbpages/rules.html')

def lbcommands(request):
    return render(request, 'sdtd/lightbringer/lbpages/commands.html')

def lbdonations(request):
    return render(request, 'sdtd/lightbringer/lbpages/donations.html')




def northshire(request):
    return render(request, 'sdtd/northshirevalley/northshiremain.html')

def nvrules(request):
    return render(request, 'sdtd/northshirevalley/nvpages/rules.html')

def nvcommands(request):
    return render(request, 'sdtd/northshirevalley/nvpages/commands.html')

def nvdonations(request):
    return render(request, 'sdtd/northshirevalley/nvpages/donations.html')




def daggerspine(request):
    return render(request, 'sdtd/daggerspine/daggerspinemain.html')

def dsrules(request):
    return render(request, 'sdtd/daggerspine/dspages/rules.html')

def dscommands(request):
    return render(request, 'sdtd/daggerspine/dspages/commands.html')

def dsdonations(request):
    return render(request, 'sdtd/daggerspine/dspages/donations.html')
