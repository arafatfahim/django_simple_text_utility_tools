from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    extras = {'name':'Arafat', 'place':'Bangladesh' }
    return render(request, 'index.html', extras)
    #return HttpResponse("<h1>HOME</h1>")

def analyze(request):
    #gettxt
    atext = request.POST.get('text', 'defult')

    #checkbox
    removepunc = request.POST.get('removepunc', 'off')
    fullcap = request.POST.get('fullcap', 'off')
    newline_remove = request.POST.get('newline_remove', 'off')
    charecter_counter = request.POST.get('charecter_counter', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    
    if removepunc == "on":
      punctuations = '''!(){}[];:'"/\,.<>@#$%^&*_-~'''
      analyzed = ""
      for char in atext:
         if char not in punctuations:
             analyzed = analyzed + char
             
      param = {'p': 'Removed Punctuations', 'analyzed_text': analyzed }
      atext = analyzed
      #return render(request, 'analyze.html', param)
      
    if(fullcap == "on"):
        analyzed = ""
        for char in atext:
            analyzed = analyzed + char.upper()
        param = {'p': 'Changed To Upper Case', 'analyzed_text': analyzed }
        atext = analyzed
        #return render(request, 'analyze.html', param)

    if(newline_remove == "on"):
        analyzed = ""
        for char in atext:
            if char !="\n" and char!="\r":
             analyzed = analyzed + char
        param = {'p': 'Remove Newline', 'analyzed_text': analyzed }
        atext = analyzed
        #return render(request, 'analyze.html', param)

    if(charecter_counter == "on"):
        analyzed = ""
        for char in atext:
             analyzed = len(analyzed)
        param = {'p': 'Character Counter', 'analyzed_text': analyzed }
        atext = analyzed
        #return render(request, 'analyze.html', param)
    
    if(spaceremove == "on"):
        analyzed = ""
        for index, char in enumerate(atext):
            if atext[index] == " " and atext[index+1]==" ":
                pass
            else:
             analyzed = analyzed + char
        param = {'p': 'Space Removed', 'analyzed_text': analyzed }
        atext = analyzed
        #return render(request, 'analyze.html', param)

    if(removepunc != "on" and newline_remove!= "on" and spaceremove != "on" and fullcap != "on"):
       return render(request, 'error.html')

    return render(request, 'analyze.html', param)

