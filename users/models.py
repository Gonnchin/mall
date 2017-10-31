from django.db import models
from db.AbstractModel import *
from utils.wrappers import *


# 用户模型管理类
class UserManager(models.Manager):

    # 通过用户名查找用户
    def user_by_username(self, username):
        try:
            return self.get(user_name=username)
        except User.DoesNotExist:
            return None

    # 将注册信息保存到数据库
    def user_register_save(self, request):
        user = User()
        user.user_name = post(request, 'user_name')
        # 密码加密   调用自定义加密函数
        user.user_pwd = password_encryption(post(request, 'user_pwd'))
        user.user_email = post(request, 'user_email')
        user.save()

    # 将地址信息保存到数据库
    def address_save(self, request):
        username = get_session(request, 'user_name')
        user = User.objects.user_by_username(username)
        user.user_recv = post(request, 'user_recv')
        user.user_addr = post(request, 'user_addr')
        user.user_email = post(request, 'user_email')
        user.user_tel = post(request, 'user_tel')
        user.user_code = post(request, 'user_code')
        user.save()


# 用户模型类
class User(AbstractModel):
    user_name = models.CharField(max_length=30)
    # 用户名密码
    user_pwd = models.CharField(max_length=70)
    user_email = models.CharField(max_length=50)
    user_tel = models.CharField(max_length=11)
    user_addr = models.CharField(max_length=50)
    # 邮政编码
    user_code = models.CharField(max_length=9)
    # 收件人
    user_recv = models.CharField(max_length=30)

    # 自定义管理器
    objects = UserManager()


# 商品浏览模型类
class RecordBrowse(AbstractModel):
    # 浏览商品
    browse_goods = models.ForeignKey('goods.Goodsinfo')
    # 浏览用户
    browse_user = models.ForeignKey(User)












