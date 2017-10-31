from django.template import Library
from django.core.urlresolvers import reverse

register = Library()


def create_menu(flag):
    menu = [
        {'name': '· 个人信息', 'link': reverse("users:index"),
         'active': flag == 'info' and 'active' or ''},
        {'name': '· 全部订单', 'link': reverse("users:order"),
         'active': flag == 'order' and 'active' or ''},
        {'name': '· 收货地址', 'link': reverse("users:address"),
         'active': flag == 'address' and 'active' or ''}
    ]

    return menu

register.filter('create_menu', create_menu)


# 浏览记录排序
@register.filter
def browse_sort(record):
    goods_list = []
    for goods in record:
        goods_list.append(goods)

    goods_list.sort(key=lambda obj: obj.updata_time, reverse=True)
    return goods_list