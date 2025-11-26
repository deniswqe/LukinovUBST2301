from django.contrib import admin
from django.urls import path, re_path
from articles import views
from articles.views import archive

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', archive, name='archive'),  
    re_path(r'^article/(?P<article_id>\d+)$', views.get_article, name='get_article'), 
]
