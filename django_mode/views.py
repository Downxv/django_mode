from django.http import HttpResponse
from django.shortcuts import render


def runoob(request):
    context = {"hello": "hello world!", "name": ["name1", "name2", "name3"], "type": {"x": "x", "y": "y"}}
    return render(request,"runoob.html", context)


def hello(request):
    return HttpResponse("hello world")
