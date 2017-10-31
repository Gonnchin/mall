from django.db import models


# 定义重新模型类
class AbstractModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    updata_time = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    # 设置为抽象类(不为其创建表)
    class Meta:
        abstract = True
