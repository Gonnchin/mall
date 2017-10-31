from django.shortcuts import render
from utils.wrappers import *
from django.http import JsonResponse
from carts.models import *
from users.models import *
from django.db import transaction
from .functions import *


# 订单主页
def index(request):
    # 获取订单中所有商品id
    goods_ids = post_list(request, 'goods_id')
    goods_list = ','.join(goods_ids)
    user_id = int(get_session(request, 'uid'))
    user = User.objects.get(id=user_id)
    carts = Cart.objects.filter(cart_goods_id__in=goods_ids, cart_user_id=user_id)
    carts.total_money = 0
    carts.total_num = 0
    for cart in carts:
        cart.single_price = cart.cart_goods.goods_price * cart.cart_num
        carts.total_money += cart.single_price
        carts.total_num += cart.cart_num
    return render(request, 'order/place_order.html', locals())


# 订单处理
@transaction.atomic
def order_handle(request):
    # 获取订单中所有商品id
    goods_str = post(request, 'goods_list')
    goods_list = goods_str.split(',')
    user_id = get_session(request, 'uid')
    # 支付方式
    goods_pay = post(request, 'goods_pay')
    carts = Cart.objects.filter(cart_goods_id__in=goods_list, cart_user_id=user_id)
    user = User.objects.get(id=user_id)

    # 设置保存点,
    save_point = transaction.savepoint()
    try:
        # 创建订单　及生成订单商品详情
        create_order(user, goods_pay, user_id, carts)
        # 事物提交
        transaction.savepoint_commit(save_point)
        return JsonResponse({'ret': 1})
    except:
            # 失败后回滚到保存点
            transaction.savepoint_rollback(save_point)
            return JsonResponse({'ret': 0})











