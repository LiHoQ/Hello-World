"""herenke URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# 配置富文本框
from django.conf import settings
import os
from django.conf.urls.static import static

# 配置VUE
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kinshow/', include('kinshow.urls')),
    path('ueditor/', include('DjangoUeditor.urls')),
    # path('', TemplateView.as_view(template_name='home.html')),  # vue配置
]

# 配置富文本框图片不能显示的问题 - 2
if settings.DEBUG:
    media_root = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=media_root)
