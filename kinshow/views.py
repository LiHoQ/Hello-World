from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404

from .models import News, NewsCategory

from django.views import generic


# def test(request):
#     a = News.objects.order_by('-title')
#     output = ', '.join([q.content for q in a])
#     return HttpResponse(a)


def index(request):
    news_all = News.objects.order_by('-pub_date')
    context = {'news_all': news_all}  # 前者对应HTML变量，后者对应views变量
    return render(request, 'kinshow/index.html', context)


# Django文档试用
# class NewsView(generic.DetailView):
#     model = News


def news(request, pk):
    news_detail = News.objects.get(pk=pk)
    return render(request, "kinshow/news_detail.html", {'news_detail': news_detail})
