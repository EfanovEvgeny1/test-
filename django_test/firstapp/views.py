from .forms import UserForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import *
from django.template.response import TemplateResponse
from .models import Person


def index(request):
    people = Person.objects.all()
    return render(request, "index.html", {"people": people})


def create(request):
    if request.method == "POST":
        klient = Person()
        klient.name = request.POST.get("name")
        klient.age = request.POST.get("age")
        klient.save()
    return HttpResponseRedirect("/")



def edit(request, id):
    try:
        person = Person.objects.get(id=id)
        
        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")


def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")




def products(request, productid):
    category = request.GET.get("cat", "")
    output = "<h2>Продукт № {0} Категория: {1}</h2>" .format(productid, category)
    return HttpResponse(output)

def users(request):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Максим")
    output = "<h2>Пользователь</h2><h3>id: {0} Имя: {1}</h3 >" .format(id, name)
    return HttpResponse(output)


def about(request):
    return HttpResponse("About")

def contact(request):
    return HttpResponseRedirect("/about")

def details(request):
    return HttpResponsePermanentRedirect("/")

def m304(request):
    return HttpResponseNotModified()

def m400(request):
    return HttpResponseBadRequest("<h2>Bad Request</h2>")

def m403(request):
    return HttpResponseForbidden ( "<h2>Forbidden</h2>")

def m404(request):
    return HttpResponseNotFound("<h2>Not Found</h2>")

def m405(request):
    return HttpResponseNotAllowed("<h2>Method is not allowed</h2>")

def m410(request):
    return HttpResponseGone("<h2>Content is no longer here</h2>")


def m500(request):
    return HttpResponseServerError("<h2>Something is wrong</h2>")
