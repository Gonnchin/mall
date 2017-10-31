from django.db import models
from db.AbstractModel import *


status = (
    (1, '待付款'),
    (2, '待发货'),
    (3, '待收货'),
    (4, '已完成'),
)

pay = (
    (1, '货到付款'),
    (2, '微信支付'),
    (3, '支付宝支付'),
    (4, '银联支付'),
)


# 创建订单模型类
class Order(AbstractModel):
    # 订单对应用户
    order_user = models.ForeignKey('users.User')
    # 付款方式
    order_pay = models.SmallIntegerField(choices=status, default=1)
    # 订单号
    order_num = models.CharField(max_length=50)
    # 收货人
    order_recv = models.CharField(max_length=20)
    # 收货地址
    order_addr = models.CharField(max_length=50)
    # 联系电话
    order_tel = models.CharField(max_length=11)
    # 订单状态
    order_status = models.SmallIntegerField(choices=pay, default=1)


# 订单商品详情
class GoodsInfoDetail(AbstractModel):
    # 商品名称
    goods_name = models.CharField(max_length=30)
    # 商品价格
    goods_price = models.DecimalField(max_digits=10, decimal_places=2)
    # 商品单位
    goods_unit = models.CharField(max_length=10)
    # 所属订单
    goods_order = models.ForeignKey(Order)
    # 商品对应图片
    goods_img = models.ImageField()
    # 商品数量
    goods_num = models.IntegerField()
