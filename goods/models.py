from django.db import models
from db.AbstractModel import *
from tinymce.models import HTMLField


# 商品分类模型
class Category(AbstractModel):
    # 名称
    cag_name = models.CharField(max_length=20)


# 自定义商品管理器类
class GoodsManager(models.Manager):
    # 获取某类商品的4个最新商品
    def new_goods(self, cag):
        return self.filter(goods_cag=cag).order_by('-id')[:4]

    # 获取某类商品中3个热门商品
    def hot_goods(self, cag):
        return self.filter(goods_cag=cag).order_by('goods_look')[:3]

    # 获取2个最新商品
    def get_new_by_all(self):
        return self.all().order_by('-id')[:2]

    # 查询某类商品中所有商品
    def get_goods_by_cag(self, cag_id, sort):
        # 根据浏览量查询
        if sort == 'hot':
            goods_list = Goodsinfo.objects.filter(goods_cag=cag_id).order_by('-goods_look')
        elif sort == 'price':
            goods_list = Goodsinfo.objects.filter(goods_cag=cag_id).order_by('goods_price')
        else:
            goods_list = Goodsinfo.objects.filter(goods_cag=cag_id)
        return goods_list


# 商品模型类
class Goodsinfo(AbstractModel):
    # 商品名称
    goods_name = models.CharField(max_length=20)
    # 商品价格
    goods_price = models.DecimalField(max_digits=8, decimal_places=2)
    # 商品图片
    goods_image = models.ImageField()
    # 商品概述
    goods_short = models.CharField(max_length=100)
    # 商品描述
    goods_describe = HTMLField(default='')
    # 商品浏览量
    goods_look = models.IntegerField(default=0)
    # 商品销售量
    goods_sales = models.IntegerField(default=0)
    # 商品状态
    goods_status = models.BooleanField(default=True)
    # 商品单位
    goods_unit = models.CharField(max_length=10)
    # 商品分类
    goods_cag = models.ForeignKey(Category)

    objects = GoodsManager()


# 广告类模型
class Advertisement(AbstractModel):
    ad_name = models.CharField(max_length=20)
    ad_image = models.ImageField(upload_to='ad')
    # 广告位链接
    ad_link = models.CharField(max_length=100)