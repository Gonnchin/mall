from utils.wrappers import *
from .models import *


def addgoods(request):
    # 获取要加入购物车的数量
    add_num = int(get(request, 'add_num'))
    # 获取商品id
    goods_id = int(get(request, 'goods_id'))
    # 获取用户id
    uid = get_session(request, 'uid')
    try:
        cart = Cart.objects.get(cart_goods=goods_id, cart_user=uid)
        cart.cart_num = (cart.cart_num + add_num)
        cart.save()
    except Cart.DoesNotExist:
        cart = Cart()
        cart.cart_user_id = uid
        cart.cart_goods_id = goods_id
        cart.cart_num = add_num
        cart.save()

    total = Cart.objects.filter(cart_user=uid).aggregate(models.Sum('cart_num'))
    return total['cart_num__sum']