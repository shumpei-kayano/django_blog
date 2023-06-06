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

# 更新処理 GETアクセスとPOSTアクセスの２パターンある
def edit(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method == 'POST':
        # POST送信されてきた場合は入力値を設定
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blogs:detail', blog_id=blog_id)
    else:
        # もともと保存されてあった内容が表⽰するためにinstance=blogを追加する
        form = BlogForm(instance=blog)
    return render(request, 'blogs/edit.html', {'form':form, 'blog':blog})
'''
ModelFormは、ModelForm(instance=インスタンス) とすることで、
あらかじめ特定のインスタンスの値を持ったフォームを表⽰させることができる
'''