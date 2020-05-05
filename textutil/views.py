# in have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def analyze(request):
    djtext = (request.POST.get('text', 'default'))
    removepunc = (request.POST.get('removepunc', 'off'))
    capitalize = (request.POST.get('capitalize', 'off'))
    analyzed = ""
    print(removepunc)
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\/,.`~!@#$%^&*_+<>?'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
    djtext = analyzed
    analyzed = ""
    if capitalize=="on":
        for char in djtext:
            analyzed = analyzed + char.upper()
    else:
        analyzed = djtext
    params={'purpose':'remove punctuation and then capitalize','analyzed_text':analyzed}
    return render(request,'analyze.html',params)