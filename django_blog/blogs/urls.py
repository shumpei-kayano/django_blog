from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:blog_id>', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('delete/<int:blog_id>/', views.delete, name='delete'), 
    path('edit/<int:blog_id>', views.edit, name='edit'), # 追加
]
