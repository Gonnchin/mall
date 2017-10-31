from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from utils.common import *
from django.http import JsonResponse
from .functions import *


def index(request):
    # 获取用户购物车内所有商品
    carts = Cart.objects.filter(cart_user=int(get_session(request, 'uid')))
    # 所有商品总价，商品总数
    carts.total_money = 0
    carts.total_num = 0
    for cart in carts:
        carts.total_num += cart.cart_num
        # 单个商品小计总价
        cart.single_price = cart.cart_goods.goods_price * cart.cart_num
        carts.total_money += cart.single_price

    return render(request, 'carts/cart.html', locals())


# 向购物车中加入商品
def add_goods(request):

    # 1.判断用户是否已登陆
    if not user_is_login(request):
        return redirect(reverse('user:login'))

    # 2.购物车内加入商品,获得总数
    total = addgoods(request)
    return JsonResponse({'total': total})


# 删除购物车中的商品
def del_cart_goods(request):
    goods_id = int(get(request, 'id'))
    user_id = int(get_session(request, 'uid'))
    try:
        cart = Cart.objects.get(cart_goods_id=goods_id, cart_user_id=user_id)
        cart.delete()
        return JsonResponse({'ret': 1})
    except Cart.DoesNotExist:
        return JsonResponse({'ret': 0})


# 修改购物车中商品数量
def update_goods(request):
    goods_id = int(get(request, 'id'))
    user_id = int(get_session(request, 'uid'))
    goods_num = get(request, 'goods_num')
    try:
        cart = Cart.objects.get(cart_goods_id=goods_id, cart_user_id=user_id)
        cart.cart_num = goods_num
        cart.save()
        return JsonResponse({'ret': 1})
    except Cart.DoesNotExist:
        return JsonResponse({'ret': 0})
