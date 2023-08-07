from django.db import models
from db.base_model import BaseModel


# Create your models here.
class OrderInfo(BaseModel):
    PAY_METHOD_CHOICES = (
        (1, "货到付款"),
        (2, "微信支付"),
        (3, "支付宝"),
    )

    ORDER_STATUS_CHOICES = (
        (1, "待支付"),
        (2, "已支付"),
        (3, "商家已接单"),
        (4, "骑手取货中"),
        (5, "订单配送中"),
        (6, "订单已完成"),
        (7, "订单已评价"),
    )

    order_id = models.CharField(max_length=128, primary_key=True, verbose_name="订单号")
    user = models.ForeignKey('apps.User', on_delete=models.CASCADE, verbose_name="用户")
    shop = models.ForeignKey('apps.Shop', on_delete=models.CASCADE, verbose_name="店铺")
    pay_method = models.SmallIntegerField(choices=PAY_METHOD_CHOICES, default=3, verbose_name="支付方式")
    total_count = models.IntegerField(default=1, verbose_name="商品数量")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="商品总价")
    shipping_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="配送费")
    order_status = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, default=1, verbose_name="订单状态")
    trade_number = models.CharField(max_length=128, default="", verbose_name="支付编号")
    comment = models.CharField(max_length=256, default="no comment yet", verbose_name="订单评论")
    invoice_head = models.CharField(max_length=256, default="no comment yet", verbose_name="发票抬头")
    taxpayer_number = models.CharField(max_length=256, default="no comment yet", verbose_name="纳税人识别号")
    order_note = models.CharField(max_length=256, default="no comment yet", verbose_name="订单备注")
    order_score = models.IntegerField(default=0, verbose_name="订单评分")

    class Meta:
        db_table = "df_order_info"
        verbose_name = "订单"
        verbose_name_plural = verbose_name


class OrderGoods(BaseModel):
    order = models.ForeignKey('OrderInfo', on_delete=models.CASCADE, verbose_name="订单")
    sku = models.ForeignKey('apps.GoodsSKU', on_delete=models.CASCADE, verbose_name="商品SKU")
    count = models.IntegerField(default=1, verbose_name="商品数量")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="商品价格")
    comment = models.CharField(max_length=256, default="no comment yet", verbose_name="商品评论")

    class Meta:
        db_table = "df_order_goods"
        verbose_name = "订单商品"
        verbose_name_plural = verbose_name


class OrderTrack(BaseModel):
    ORDER_STATUS_CHOICES = (
        (1, "待支付"),
        (2, "已支付"),
        (3, "商家已接单"),
        (4, "骑手取货中"),
        (5, "订单配送中"),
        (6, "订单已完成"),
        (7, "订单已评价"),
    )

    order = models.ForeignKey('OrderInfo', on_delete=models.CASCADE, verbose_name="订单")
    order_status = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, default=1, verbose_name="订单状态")

    class Meta:
        db_table = "df_order_track"
        verbose_name = "订单轨迹"
        verbose_name_plural = verbose_name


class OrderComment(BaseModel):
    order = models.ForeignKey('OrderInfo', on_delete=models.CASCADE, verbose_name="订单")
    image = models.ImageField(upload_to='comment', verbose_name="图片路径")

    class Meta:
        db_table = "df_order_comment"
        verbose_name = "订单评论图片"
        verbose_name_plural = verbose_name
