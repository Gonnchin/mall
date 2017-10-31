from django.db import models
from db.AbstractModel import *


# 自定义购物车管理器类
class CartManager(models.Manager):

    # 根据用户id查询购物车内数量
    def get_cart_num(self, user_id, add_num):
        cart = self.filter(cart_user=user_id)
        total = cart.cart_num + add_num
        cart.cart_num = total
        return total


# 购物车模型类
class Cart(AbstractModel):
    # 购物车内的商品
    cart_goods = models.ForeignKey('goods.Goodsinfo')
    # 该商品数量
    cart_num = models.IntegerField(default=0)
    # 购物车对应的用户
    cart_user = models.ForeignKey('users.User')

    objects = CartManager()