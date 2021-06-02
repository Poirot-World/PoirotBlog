from django.db import models
from django.utils import timezone
'''
Post是一个对象。
所有的Model都必须继承自django.db.models.Model。
Model中所有的字段都是django.db.models.Field 的子类。（字段表示与对象或类关联的变量。）
Post定义了5个类属性，分别是ForeignKey（指向另一个模型的连接），
CharField（如何用为数有限的字符来定义一个文本），
TextField（这是没有长度限制的长文本）
和DateTimeField（日期和时间）类型。

Post定义了2个方法。
publish()是发表Post。
__str__用来优化打印Model实例的样式
'''


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(
    default = timezone.now)
    published_date = models.DateTimeField(
    blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
