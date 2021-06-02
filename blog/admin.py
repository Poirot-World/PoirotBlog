from django.contrib import admin
from .models import Post  #导入Post模型
'''
为了让我们的模型在admin页面上可见，需要用下列语句来注册模型
'''
# Register your models here.
admin.site.register(Post)
