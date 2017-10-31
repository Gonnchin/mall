from .models import *
from utils.common import *
from users.models import *
from django.core.paginator import Paginator
from carts.models import *


# 获取所有分类
def get_cags():
    cags = Category.objects.all()
    # 遍历所有分类，获取每类中的最新商品
    for cag in cags:
        new = Goodsinfo.objects.new_goods(cag)
        hot = Goodsinfo.objects.hot_goods(cag)
        # 给cag类添加热门商品属性，和最新商品属性
        cag.newgoods = new
        cag.hotgoods = hot
    return cags


# 添加用户的浏览记录
def ubrowse_record(request):
    # 1.判断用户是否登录
    if not user_is_login(request):
        return

    # 2.获取用户id,商品id
    uid = get_session(request, 'uid')
    gid = get(request, 'id')

    # 3.查询表是否有该条记录
    try:
        # 如果该记录存在直接更新
        record = RecordBrowse.objects.get(browse_goods=gid, browse_user=uid)
        record.save()
    except RecordBrowse.DoesNotExist:
        records = RecordBrowse.objects.filter(browse_user=uid).order_by('updata_time')
        # 如果无浏览记录或　浏览记录小于5,新增记录　
        if records == '' or len(records) < 5:
            rcd = RecordBrowse()
            rcd.browse_goods_id = gid
            rcd.browse_user_id = uid
            rcd.save()
        # 大于5 更新最早的记录
        elif records.count() >= 5:
            records[0].browse_goods_id = gid
            records[0].browse_user_id = uid
            records[0].save()


# 分页
def pagination(goods_list, pag_id):
    # 分页显示
    paginator = Paginator(goods_list, 5)
    # 获取指定页码数据
    current_pag = paginator.page(pag_id)
    page_id = int(pag_id)
    return paginator, current_pag, page_id


# 统计购物车中的数量
def get_num_in_cart(view_func):
    def wrapper(request, *args, **kwargs):
        carts = Cart.objects.filter(cart_user=int(get_session(request, 'uid')))
        if carts:
            request.total_num = 0
            for cart in carts:
                request.total_num += cart.cart_num
        return view_func(request, *args, **kwargs)
    return wrapper