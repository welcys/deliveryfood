from django.contrib.auth.models import AbstractUser
from django.db import models
from db.base_model import BaseModel


# Create your models here.

class User(AbstractUser, BaseModel):
    """用户模型类"""
    gender = models.BooleanField(default=False, verbose_name='性别')
    phone_number = models.CharField(max_length=11, verbose_name='手机号')
    profile_image = models.ImageField(upload_to='user', verbose_name='用户头像')
    real_name = models.CharField(max_length=20, verbose_name='真实姓名')

    class meta:
        db_table = 'df_user'  # 指定表名
        verbose_name = '用户'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称


class Address(BaseModel):
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='所属账户')
    receiver = models.CharField(max_length=20, verbose_name='收件人')
    addr = models.CharField(max_length=256, verbose_name='收件地址')
    zip_code = models.CharField(max_length=6, null=True, verbose_name='邮政编码')
    contact_phone = models.CharField(max_length=11, verbose_name='联系电话')
    is_default = models.BooleanField(default=False, verbose_name='是否默认')
    lng = models.FloatField(default=0, verbose_name='经度')
    lat = models.FloatField(default=0, verbose_name='纬度')

    class meta:
        db_table = 'df_address'
        verbose_name = '地址'
        verbose_name_plural = verbose_name


class Shop(BaseModel):
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='所属账户')
    shop_name = models.CharField(max_length=20, verbose_name='店铺名称')
    shop_addr = models.CharField(max_length=256, verbose_name='店铺地址')
    shop_type = models.CharField(max_length=20, verbose_name='店铺类型')
    type_detail = models.CharField(max_length=20, verbose_name='店铺详细类型')
    shop_score = models.FloatField(default=0, verbose_name='店铺评分')
    shipping_price = models.FloatField(default=0, verbose_name='配送费')
    shop_sales = models.IntegerField(default=0, verbose_name='店铺销量')
    shop_image = models.ImageField(upload_to='shop', verbose_name='店铺图片')
    order_start = models.IntegerField(default=0, verbose_name='接单时间')
    order_end = models.IntegerField(default=0, verbose_name='接单结束时间')
    is_open = models.BooleanField(default=False, verbose_name='是否营业')
    rating_level = models.CharField(max_length=20, verbose_name='好评度')

    class meta:
        db_table = 'df_shop'
        verbose_name = '店铺'
        verbose_name_plural = verbose_name


class UserImage(BaseModel):
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='所属账户')
    image = models.ImageField(upload_to='user', verbose_name='用户图片')

    class meta:
        db_table = 'df_user_image'
        verbose_name = '用户图片'
        verbose_name_plural = verbose_name


class ShopImage:
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE, verbose_name='所属店铺')
    image = models.ImageField(upload_to='shop', verbose_name='店铺图片')

    class meta:
        db_table = 'df_shop_image'
        verbose_name = '店铺图片'
        verbose_name_plural = verbose_name


class ShopTypeDetail(BaseModel):
    type_code = models.CharField(max_length=20, verbose_name='类型代码')
    type_name = models.CharField(max_length=20, verbose_name='类型名称')

    class meta:
        db_table = 'df_shop_type'
        verbose_name = '店铺详细类型'
        verbose_name_plural = verbose_name


