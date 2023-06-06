from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm
from django.views.decorators.http import require_POST # 追加

# トップページ
def index(request):
    blogs = Blog.objects.order_by('-created_datetime')
    return render(request, 'blogs/index.html', {'blogs':blogs })

# 記事詳細ページ
def detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'blogs/detail.html', {'blog':blog})

# 新規作成ページ
def new(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    else:
        form = BlogForm
    return render(request, 'blogs/new.html', {'form':form})

# 削除処理 URLアクセスではなく、削除ボタンでPOSTアクセスしたときに実行
@require_POST
def delete(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect('blogs:index')