from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView



def home(request):
    return render(request, 'home.html')


def my_logout(request):
    logout(request)
    return redirect('home')


class HomePageView(TemplateView):
    template_name = "home3.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["minha_variavel"] = "Ola seja bem vindo a página do João "
        return context
    
    template_name = "home4.html"

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context["teste"] = "jsjsjsjssj"
        return context
    

class MyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home3.html")
    
#Class Based View

    

    def post(self, request, *args, **kwargs):
        return HttpResponse("home2.html") 