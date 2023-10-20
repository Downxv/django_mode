import datetime

from django.core.paginator import Paginator
from django.db.models import Max, Min, Sum, Avg, Count
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse

from .models import User, Man, Movie, People


# Create your views here.
def sub(request):
    print(request.method)
    print(request.GET.get("name"))
    print(request.GET.getlist("name"))
    print(request.POST)
    print(request.path)
    print(request.COOKIES)
    print(request.session)
    print(request.FILES) # 文件上传
    print(request.META)
    rp = JsonResponse({'sub': 'sub'})
    rp.set_cookie('a', 1, max_age=10)
    rp.set_cookie("b", 2, expires=datetime.datetime.now())
    rp.delete_cookie('b')
    request.session['uid'] = 1
    request.session.set_expiry(7*24*3600)
    session_key = request.session.session_key
    # request.session.delete(session_key)
    print(session_key)
    return rp


def get_user(request):
    user = User.objects.all().order_by('-id', 'age')
    for i in user:
        print(i.name)
    print(Man.objects.all()[1:3].values('name', 'age'))
    print(Man.objects.all().values_list('name', 'age'))
    # Man.objects.filter(uid__gt=2, uid__lte=6, uid__in=[3, 4])
    # Man.objects.filter(name__contains="li")
    # Man.objects.filter(name__icontains="li") 大小写不敏感
    # Man.objects.filter(name__regex="sd$")
    # Man.objects.filter(name__iregex="sd$")
    # Man.objects.filter(age__range=[10, 20]).order_by('-uid')
    # Man.objects.exclude(age__in=[1,2])
    # Man.objects.filter(name__startswith="l“)
    # Man.objects.filter(name__endswith="l“)
    # Man.objetcs.aggregate(Max('age'))
    # Man.objetcs.aggregate(Min('age'))
    # Man.objetcs.aggregate(Sum('age'))
    # Man.objetcs.aggregate(Avg('age'))
    # Man.objetcs.aggregate(Count('age'))
    # try:
    #   Man.objects.create(name="lisi")
    #   Man.objects.first().delete()
    #   Man.objects.first().update(age=1)
    # Man.objects.last()
    # Man.objects.count()
    # Man.objects.get()
    # Man.objects.exists()
    # except:
    #     pass
    # 分页功能
    # u = User.objects.all()
    # p = Paginator(u, 10)
    # o = p.page(2)
    # pr = p.page_range
    # 一对多
    # q = Man.objects.get(name='1')
    # User.objects.create(name="q", uuid=q)
    # Man.objects.all().delete() 会删除user对应的数据
    # 正向查询
    # User.objects.get().uuid.name
    # User.objects.filter(Man__name='1')
    # 反向查询
    # Man.objects.user_set.all()
    # 一对一反向查询
    # Man.objects.user.all()
    # 多对多
    # p = People.objects.get()
    # m = Movie.objects.get()
    # p.movies.add(m)
    # m.people_set.add(p)
    # p.movies.filter().delete()
    # m.people_set().filter().delete()
    
    return HttpResponse("ok")


def chuancan(request, **kwargs):
    print(kwargs)
    return HttpResponse(str(kwargs))


def chongdinxiang(request):
    return redirect(reverse("user_app:chuancan", kwargs={"uid": 12, "gid": 21, "name": "ok"}))


def moban(request):
    data = {
        "name": "zhangsan",
        "age": 12,
        "like": ["movie", "game", "code"],
        "address": {"city": "深圳", "province": "广东"},
        "stars": [
            ["马化腾", "马云"],
            ["雷军", "马斯克"]
        ]
    }
    return render(request,"moban.html", data)


def block(request):
    return render(request, "block.html")


def child(request):
    return render(request, "child.html")