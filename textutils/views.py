# I have created this file harry

from django.http import HttpResponse
from django.shortcuts import render
#code for video 6
#def index(request):
  #  return HttpResponse('''<h1>Hello sarthak</h1> <a href="https://www.youtube.com/watch?v=Jksh4plnL5k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=15&ab_channel=CodeWithHarry">youtube</a>''')

#def about(request):
  #  return HttpResponse()

#def footer(request):
  #  return HttpResponse("How i  can help u")

#code for video 7

def ex1(request):
    s="<h1> welcome to Navigation bar</h1><br>" \
      "<a href="">facebook</a><br>" \
      "<a href="">youtube</a><br>" \
      "<a href="">google</a><br>" \
      "<a href="">yahoo</a>"
    return  HttpResponse(s)


def example2(request):
     return HttpResponse('''<h1 style="text-align:center;font-size:50px;color:red;position:relative;top:200px">does not find any punctuations</h1>''')


def index(request):

    return render(request,'index.html')
   # return HttpResponse("Home")

def analyze(request):
    #Get the text
    djtext=request.GET.get('text','default')

    #cheak cheakbox value
    fullcaps=request.GET.get('fullcaps','off')
    removepunc=request.GET.get('removepunc','off')
    newlineremover=request.GET.get('newlineremover','off')
    extrasapaceremover=request.GET.get('extrasapaceremover','off')
    charcounter=request.GET.get('charcounter','off')

    

   #cheak which cheakbox is on
    if removepunc=="on":

       # analyzed=djtext
       punctuations='''!()-[]{},:'"\,<>./?@#$%^&*_~'''
       analyzed= " "
       for char in djtext:
           if char  not in punctuations:
               analyzed=analyzed+char
       params={'purpose':'please remove punctuations','analyzing_text':analyzed}

       # Analyze the text

       return render(request,'analyze.html',params)

    elif fullcaps=="on":
       analyzed=" "
       for char in djtext:
         analyzed=analyzed+char.upper()

         params={'purpose':'I want to capitslize it','analyzing_text':analyzed}
       return render(request,'analyze.html',params)

    elif newlineremover=="on":
       analyzed=" "
       for char in djtext:
          if char!="\n":
            analyzed=analyzed+char

          params={'purpose':'Remove new line','analyzing_text':analyzed}
       return render(request,'analyze.html',params)


    elif extrasapaceremover=="on":
        analyzed=" "
        for index,char in enumerate(djtext):
           if not(djtext[index]==" " and  djtext[index+1]==" "):
            analyzed=analyzed+char

           params={'purpose':'Remove space','analyzing_text':analyzed}
        return render(request,'analyze.html',params)

    elif charcounter=="on":
      count=0
      for i in djtext:
         if i == 'abcdefghijklmnopqrstuvwxyz':
          count=count+i
         
         params={'purpose':'character counter','analyzing_text':count}
         return render(request,'analyze.html',params)




    else:
      return HttpResponse('''<h1 style="text-align:center;font-size:50px;color:red;position:relative;top:200px">does not find any punctuations</h1>''')




    #Analyze the text
#     return  HttpResponse("remove punc")
# def capitalizefirst(request):
#     return HttpResponse("capitalizefirst")
# def newlineremove(request):
#     return HttpResponse("new line remove")
# def spaceremove(request):
#     return HttpResponse("Space remover <a href='/'>back</a>")
# def counter(request):
#     return HttpResponse("counter called")