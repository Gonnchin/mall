from django.shortcuts import render
from .functions import *
from utils.wrappers import *
from carts.models import *


def query(request):
    return render(request, 'booktest/query.html')

#  商品主页
@get_num_in_cart
def index(request):

    # 获取所有分类
    cags = get_cags()

    # 获取所有广告(元组)
    ad = Advertisement.objects.all()
    ad1 = ad[:4]
    ad2 = ad[4:6]

    return render(request, 'goods/index.html', locals())


# 商品详情
@get_num_in_cart
def detail(request):
    # 获取对应goods对象
    goods = Goodsinfo.objects.get(id=get(request, 'id'))
    # 获取两个最新商品
    best_new_goods = Goodsinfo.objects.get_new_by_all()
    # 用户的浏览记录
    ubrowse_record(request)
    goods_id = get(request, 'id')
    return render(request, 'goods/detail.html', locals())


# 商品列表页
@get_num_in_cart
def list(request, cag_id, pag_id):
    # 获取两个最新商品
    best_new_goods = Goodsinfo.objects.get_new_by_all()
    # 获取所有分类
    cags = get_cags()
    show = get(request, 'show')
    # 获得分类下的所有商品
    goods_list = Goodsinfo.objects.get_goods_by_cag(cag_id, show)
    # 分页，获取当前页, 请求页码
    paginator, current_page, page_id = pagination(goods_list, pag_id)
    return render(request, 'goods/list.html', locals())