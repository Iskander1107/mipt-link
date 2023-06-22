from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from links.models import Links


def links_redirect(request, lnk):
    redirect_to = Links.objects.filter(link=lnk).first()
    redirect_to.visited_times += 1
    redirect_to.save()
    return redirect(redirect_to.link_to)


def index(request):
    return HttpResponse('INDEX PAGE')