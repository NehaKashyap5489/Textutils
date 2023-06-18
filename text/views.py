from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #params={'name':'Neha','city':'Delhi'}
    return render (request,'index.html')
    #return HttpResponse ("Home")

def removepunc(request):
    #getting the text
    djtext=request.GET.get('text','default')
    #chack checkvalue 
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')
    charcount=request.GET.get('charcount','off')
    # print(removepunc)
    # print(djtext)
    if removepunc == "on":
        puctuations='''`~!@#$%^&*()-_=+[]\;',./{}|:"<>?'''
        analyzed=""
        for i in djtext:
            if i not in puctuations:
                analyzed=analyzed+i

        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed
        #return render (request,'removepunc.html',params)
    
    
    if (fullcaps=='on'):
        analyzed=""
        for i in djtext:
            analyzed=analyzed+ i.upper()
        params={'purpose':'Changes to Uppercase','analyzed_text':analyzed}
        djtext=analyzed

        #return render (request,'removepunc.html',params)
    if (newlineremover=='on'):
        analyzed=""
        for i in djtext:
            if i !='/n':
                analyzed=analyzed+i        
        params={'purpose':'New line removed','analyzed_text':analyzed}
        djtext=analyzed
        #return render (request,'removepunc.html',params)
    if (extraspaceremover=='on'):
        analyzed=""
        for index,i in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed=analyzed+i          
        params={'purpose':'Extra space Removed','analyzed_text':analyzed}
        djtext=analyzed
        #return render (request,'removepunc.html',params)
    if (charcount=='on'):
        analyzed=0
        for i in djtext:
            analyzed+=1
        params={'purpose':'Charter Counted','analyzed_text':analyzed}
        #return render (request,'removepunc.html',params)
    # else:
    if (removepunc!='on' and fullcaps!='on' and extraspaceremover!='on' and newlineremover!='on' and charcount!='on'):
        return HttpResponse('Please Select any operation and try agaian')

    return render (request,'removepunc.html',params)

