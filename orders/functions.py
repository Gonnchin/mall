from .models import *
import time
import random


def create_order(user, goods_pay, user_id, carts):

    # 生成订单表
    order = Order()
    order.order_user = user
    order.order_addr = user.user_addr
    order.order_recv = user.user_recv
    order.order_tel = user.user_tel
    order.order_pay = goods_pay
    order.order_num = str(user_id) + str(int(time.time())) + str(random.randint(1111, 99999))
    order.save()

    # 生成订单详情表
    for cart in carts:
        goods = GoodsInfoDetail()
        goods.goods_name = cart.cart_goods.goods_name
        goods.goods_img = cart.cart_goods.goods_image
        goods.goods_price = cart.cart_goods.goods_price
        goods.goods_unit = cart.cart_goods.goods_unit
        goods.goods_order = order
        goods.goods_num = cart.cart_num
        goods.save()
        cart.delete()