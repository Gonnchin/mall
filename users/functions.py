import re
from .models import *
from utils.wrappers import *
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from utils.common import *


# 验证用户注册信息
def check_register_info(request):
    user_name = post(request, 'user_name')
    user_pwd = post(request, 'user_pwd')
    user_pwd2 = post(request, 'user_pwd2')
    user_email = post(request, 'user_email')
    flag = True
    # 验证用户名
    if not(5 <= len(user_name) <= 20):
        flag = False
        add_message(request, 'user_name', '用户名长度在5-20之间')

    # 验证密码
    if not(8 <= len(user_pwd) <= 20):
        flag = False
        add_message(request, 'user_pwd', '密码长度在8-20之间')

    # 检测两次密码输入是否一致
    if user_pwd != user_pwd2:
        flag = False
        add_message(request, 'user_pwd', '两次密码不一致')

    # 检测邮箱格式是否合法
    reg = '^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$'
    if not re.match(reg, user_email):
        flag = False
        add_message(request, 'user_email', '邮箱格式不和法')

    # 检测用户名是否已经存在
    # if User.objects.user_by_username(user_name):
    #     flag = False
    #     add_message(request, 'user_name', '用户名已经存在!')
    return flag


# 验证用户登陆信息
def check_logon_info(request):
    user_name = post(request, 'user_name')
    print('------12', post(request, 'user_pwd'))
    user_pwd = password_encryption(post(request, 'user_pwd'))
    print('---11', user_name, user_pwd)
    # 进行基本验证
    if not (5 <= len(user_name) <= 20):
        add_message(request, 'user_name', '用户名不正确')
        return False
    # 查询并获取该用户
    user = User.objects.user_by_username(user_name)
    # 判断用户是否存在
    if not user:
        add_message(request, 'user_name', '用户名不正确')
        return False
    else:
        if user.user_pwd == user_pwd:
            return user
        else:
            add_message(request, 'user_pwd', '用户名或密码不正确')
            return False


# 验证用户是否存在
def user_exist(request):
    user_name = get(request, 'user_name')
    user = User.objects.user_by_username(user_name)
    return user


# 记录用户名
def remember_name(response, request, user_name):
    reme = post(request, 'reme_name')
    if reme:
        set_cookie(response, 'user_name', user_name)


# 记录登陆状态
def keep_status(request, user_name):
    user = User.objects.filter(user_name=user_name)[0]
    set_session(request, 'user_name', user_name)
    set_session(request, 'uid', user.id)


# 获取跳转的url
def get_redirect_url(request):
    per_url = get_session(request, 'pre_url')
    if per_url:
        return per_url
    else:
        return reverse('goods:index')


# 用户权限验证
def check_permissios(view_func):
    def wrapper(request, *args, **kwargs):
        # if get_session(request, 'user_name'):
        if user_is_login(request):
            return view_func(request, *args, **kwargs)
        else:
            return redirect(reverse('users:login'))
    return wrapper


# 校验地址信息
def check_addr(request):
    user_recv = post(request, 'user_recv')
    user_addr = post(request, 'user_addr')
    user_code = post(request, 'user_code')
    usr_tel = post(request, 'user_tel')
    if not 0 < len(user_recv) <= 20:
        return False
    if len(user_addr) == 0:
        return False
    if len(user_code) != 6:
        return False
    if len(usr_tel) != 11:
        return False
    return True












