# i create this file - hari om
from django import http
from django.http import HttpResponse

# imports
from django.shortcuts import render, resolve_url

# def index(req):
#     return HttpResponse("hello world")

# html page
def index(req):
    return render(req, "index.html")


def about(req):
    return render(req, "about.html")


# def about(req):
#     return HttpResponse("this is about page")


# def link(req):
#     return HttpResponse("<a href=https://www.amazon.in>amazon</a>")


# project

# PIPELINE FOR OUR TEXTUIILS PROJECT

# capitalize the first word
def capFirst(req):
    return HttpResponse("capFirst")


# remove punch
def removePunc(req):
    # get the text from home
    djText = req.GET.get("text", "default")
    # show the text value
    return HttpResponse(djText)


# newline remove
def newlineremove(req):
    return HttpResponse("newline remove")


# space remove
def spaceremove(req):
    return HttpResponse("space remover")


# char count
def charcount(req):
    return HttpResponse("char count")
