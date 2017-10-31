from django.test import TestCase
from .models import *
import random
#
# 创建分类
# cags = ['新鲜水果', '海鲜水产', '猪牛羊肉', '禽类蛋品', '新鲜蔬菜', '速冻食品']
# for cag in cags:
#     c = Category()
#     c.cag_name = cag
#     c.save()
#
# units = ['500克', '20克', '3条', '1根', '1个', '1顿', '1包']
#
#
#
# with open('/home/python/Desktop/mall/data.txt', 'r') as f:
#     for name in f:
#         goods = Goodsinfo()
#         goods.goods_name = name[:-1]
#         goods.goods_short = '草莓浆果柔软多汁，味美爽口，适合速冻保鲜贮藏。草莓速冻后，可以保持原有的色、香、味，既便于贮藏，又便于外销。'
#         goods.goods_price = random.randint(60, 400)
#         goods.goods_describe = """草莓采摘园位于北京大兴区 庞各庄镇四各庄村 ，每年1月-6月
#         面向北京以及周围城市提供新鲜草莓采摘和精品礼盒装草莓，草莓品种多样丰富，个大香甜。所
#         有草莓均严格按照有机标准培育，不使用任何化肥和农药。草莓在采摘期间免洗可以直接食用。
#         欢迎喜欢草莓的市民前来采摘，也欢迎各大单位选购精品有机草莓礼盒，有机草莓礼盒是亲朋馈
#         赠、福利送礼的最佳选择。"""
#         goods.goods_cag_id = random.randint(1, 6)
#         goods.goods_unit = units[random.randint(0, len(units) - 1)]
#         goods.goods_image = 'goods/' + str(random.randint(1, 18)) + '.jpg'
#         goods.save()

# 插入广告数据
# for i in range(1, 5):
#     ad = Advertisement()
#     ad.ad_name = '广告位'
#     ad.ad_link = '#'
#     ad.ad_image = 'goods/ad/slide0' + str(i) + '.jpg'
#     ad.save()
#
#
# for i in range(1, 3):
#     ad = Advertisement()
#     ad.ad_name = '广告位'
#     ad.ad_image = 'goods/ad/adv0' + str(i) + '.jpg'
#     ad.ad_link = '#'
#     ad.save()