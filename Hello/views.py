# This file is created by me manually

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyse(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    new_line = request.POST.get('new_line', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercount = request.POST.get('charactercount', 'off')
    punctution = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''


    if removepunc == "on":
        analysed = ""
        for char in djtext:
            if char not in punctution:
                analysed = analysed + char

        analyser = {'purpose':'Removing punctution', 'analysed_text':analysed}
        djtext = analysed


    if capitalize == "on":
        analysed = ""
        for char in djtext:
            analysed = analysed + char.upper()

        analyser = {'purpose':'Capitalizing your text', 'analysed_text':analysed}
        djtext = analysed


    if new_line == 'on':
        analysed = ""
        for char in djtext:
            if char != "\n":
                analysed = analysed + char
        analyser = {'purpose': 'New line Remover', 'analysed_text': analysed}
        djtext = analysed


    if extraspaceremover == 'on':
        analysed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analysed = analysed + char
        analyser = {'purpose': 'Extra Space Remover', 'analysed_text': analysed}
        djtext = analysed


    if charactercount == 'on':
        analysed = ""
        couttt = 0
        for char in djtext:
            couttt += 1
        for char in djtext:
            analysed = analysed + char
        analyser = {'purpose':'Counting character', 'analysed_text':analysed, 'counting':f"Total character are {couttt}"}


    if removepunc != 'on' and capitalize != 'on' and extraspaceremover != 'on' and charactercount != 'on':
        return HttpResponse("You have not choosen any operation kindly choose a operation from the previous tab")

    return render(request, 'analyser.html', analyser)

def contact(request):
    return render(request, 'contact.html')

