
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    chactercount=request.POST.get('chactercount', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'exteraspaceremover', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if(chactercount=='on'):
        analyzed=''
        x=len(djtext)
        params = {'purpose': 'chactercount', 'analyzed_text': analyzed}
        print('the length of djtext',x)


    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and chactercount!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)
