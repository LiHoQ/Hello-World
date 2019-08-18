from django.db import models

from DjangoUeditor.models import UEditorField

# Create your models here.


class NewsCategory(models.Model):
    name = models.CharField("新闻分类", max_length=255)
    pub_date = models.DateTimeField("发布时间", auto_now_add=True)
    update_time = models.DateTimeField("最后修改时间", auto_now=True)
    cover_pic = models.ImageField("封面图片", blank=True, null=True)
    note = models.CharField("备注", max_length=255, blank=True, null=True)
    status = models.BooleanField("状态", default=True)
    sort = models.IntegerField("排序", unique=True, blank=True, null=True)
    backup = models.CharField("预留", max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "news_category"
        ordering = ["id"]
        verbose_name_plural = "新闻分类"


class News(models.Model):
    title = models.CharField('标题', max_length=255)
    author = models.CharField('作者', max_length=255, default='佚名')
    news_category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    pub_date = models.DateTimeField("发布时间", auto_now_add=True)
    update_time = models.DateTimeField("最后修改时间", auto_now=True)
    content = UEditorField("新闻内容", width=840, height=400, toolbars='full',
                           imagePath="images/", filePath="files/",
                           upload_settings={'imageMaxSize': 1204000 * 10},
                           settings={}, error_messages={'null': "不能为空."})
    word_num = models.IntegerField('字数', blank=True, null=True)
    browse_num = models.IntegerField("浏览数", blank=True, null=True)
    status = models.BooleanField("状态", default=True)
    sort = models.IntegerField("排序", blank=True, null=True, unique=True)
    level = models.IntegerField('level', blank=True, null=True)  # 数据结构知识，可以固定各类范围
    description = models.CharField("描述", max_length=255, blank=True, null=True)
    file = models.FileField("附件", blank=True, null=True)
    cover_pic = models.ImageField("封面图片", blank=True, null=True)  # upload_tp优先级没有富文本框高
    backup = models.CharField("预留", max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

    # 元选项
    class Meta:
        # 数据库表名
        db_table = "news_info"
        # 排序，默认升序，降序前面加-
        ordering = ["id"]
        # 在admin中显示的名称
        verbose_name_plural = "新闻"