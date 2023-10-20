from django.urls import path, re_path
from user_app.views import *


urlpatterns = [
    path('sub/', sub, name="sub"),
    path('user/', get_user, name="get_user"),
    path('chuancan/<int:uid>/<int:gid>/<str:name>', chuancan, name="chuancan"),
    # 以前的写法
    # re_path('chuancan/?P<uid>\d+/?P<gid>\d+>/?P<name>\w+', chuancan, name="chuancan"),
    path('chongdinxiang/', chongdinxiang, name="chongdinxiang"),
    path('moban/', moban, name="moban"),
    path('block/', block, name="block"),
    path('child/', child, name="child"),
]