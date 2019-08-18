from django.contrib import admin

# Register your models here.

from kinshow.models import News, NewsCategory


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    # 列表页属性
    list_display = ["title", "news_category",  "description", "content", 'pk']  # 显示字段
    list_filter = ["news_category"]  # 过滤字段，会出现选项栏
    search_fields = ["description"]  # 按内容搜索的字段
    list_per_page = 5  # 分页
    # 修改页属性
    fieldsets = [
        ("基本内容", {"fields": ["title", "description", "cover_pic", "news_category", "content"]}),
        ('新闻状态', {'fields': ['status']}),
    ]  # 给属性分组，并显示可修改内容


class NewsInline(admin.TabularInline):
    model = News
    extra = 1  # 这里是news的个数


class NewsCategoryAdmin(admin.ModelAdmin):
    # 列表页属性
    list_display = ["id", "name", "note", "pub_date"]  # 显示字段
    list_filter = ["name"]  # 过滤字段
    search_fields = ["name"]  # 按内容搜索字段
    list_per_page = 5  # 分页
    fields = ["note", "name", "status", "sort"]

    inlines = [NewsInline]
    actions_on_top = False
    actions_on_bottom = True


admin.site.register(NewsCategory, NewsCategoryAdmin)
