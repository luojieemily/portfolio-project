from django.shortcuts import render, get_object_or_404

from .models import Blog

def allblogs(request):
    blogs =Blog.objects.all().order_by('-pub_date')  #all().order_by('-pub_date')为Emily手工添加，为blog按日期排序，但网上有说多了会比较慢
    return render(request, 'blog/allblogs.html', {'blogs': blogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html',{ 'blog': detailblog})