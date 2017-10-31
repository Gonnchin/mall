from django.shortcuts import render,redirect
from .functions import *
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from orders.models import *
from django.core.paginator import Paginator


# 用户注册页面
def register(request):
    info = get_messages(request)
    return render(request, 'users/register.html', locals())


# 用户登陆页面
def login(request):
    info = get_messages(request)
    return render(request, 'users/login.html', locals())


# 用户中首页
# 需要优化
@check_permissios
def user_info(request):
    # 获取user对象
    user = User.objects.user_by_username(get_session(request, 'user_name'))
    user_name = request.session.get('user_name', '')
    user_pwd = request.session.get('user_pwd')
    return render(request, 'users/user_center_info.html', locals())


# 用户中心订单页面
@check_permissios
def user_order(request):
    user_id = get_session(request, 'uid')
    # 获得所有订单
    orders = Order.objects.filter(order_user_id=user_id)

    # 计算订单金额
    for order in orders:
        order.total_money = 0
        for goods in order.goodsinfodetail_set.all():
            order.total_money += goods.goods_price * goods.goods_num

    # 订单显示 分页
    paginator = Paginator(orders, 3)
    page_num = get(request, 'pag')
    if not page_num:
        page_num = 1
    pag_orders = paginator.page(page_num)
    return render(request, 'users/user_center_order.html', locals())


# 用户中心地址页面
@check_permissios
def user_address(request):
    # 获取user对象
    user = User.objects.user_by_username(get_session(request, 'user_name'))
    return render(request, 'users/user_center_site.html', locals())


# 处理注册信息
def register_handle(request):
    # 校对注册信息
    if check_register_info(request):
        # 1.信息符合要求,信息入库
        User.objects.user_register_save(request)
        # 跳转登陆页面
        return redirect(reverse('users:login'))
    else:
        # 2.验证失败,跳转注测页面
        return redirect(reverse('users:register'))


# 验证用户是否存在
def check_exist(request):
    if user_exist(request):
        return JsonResponse({'ret': True})
    else:
        return JsonResponse({'ret': False})


# 验证登陆信息
def login_handle(request):
    user = check_logon_info(request)
    # 1.登陆信息正确
    if user:
        # 获取跳转的url
        url = get_redirect_url(request)
        response = redirect(url)
        # 记住用户名
        remember_name(response, request, user.user_name)
        # 记住登陆状态
        keep_status(request, user.user_name)
        return response
    # 2.登陆信息不正确
    else:
        return redirect(reverse('users:login'))


# 退出登录
def logoff(request):
    # 退出后还在当前页面
    url = get_redirect_url(request)
    del_session(request)
    return redirect(url)


# 校验地址信息
def addr_handle(request):
    if check_addr(request):
        # 信息入库
        User.objects.address_save(request)
    return redirect(reverse('users:address'))