from django.db import models



class Expense(models.Model):
    
    CATE_CHOICES = [
      (0, "未分類"),
      (1, "飲食"),
      (2, "衣服"),
      (3, "交通"),
      (4, "教育"),
      (5, "娛樂"),
      (99, "其它"),
    ]
    
    item     = models.CharField('項目', max_length=30)
    category = models.IntegerField('支出類別', default=0, choices=CATE_CHOICES)
    amount   = models.IntegerField('支出金額', default=0)
    time     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item