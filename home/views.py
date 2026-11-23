from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Teste Django')

def sobre(request):
    return HttpResponse('<h1>Sistema 2.0 desenvolvido por mim mesmo, com Django</h1>')

def contato(request):
    return HttpResponse('Esta é a página de contato')

def ajuda(request):
    return HttpResponse('Esta é a página de ajuda')