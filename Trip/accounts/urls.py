from django.conf.urls import url
from django.urls import path,include
from . import views
from .views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
        path('', views.base, name='base'),
        path('articles/', views.articles, name='articles'),
        path('comment/newest_articles/', views.newest_articles, name='newest_articles'),
        path('comment/oldest_articles/', views.oldest_articles, name='oldest_articles'),
        path('articles/<str:tittle>/', views.detail_article),
        path('articles/delete/<int:id>/', views.delete_article, name='delete_articles'),
        path('articles_edit/<int:id>/', views.edit_article, name='edit_articles'),
        path('comments/', views.comments, name='comments'),
        path('comment/newest_comment/<str:tittle>/', views.newest_comment, name='newes_commentt'),
        path('comment/oldest_comment/<str:tittle>/', views.oldest_comment, name='oldest_comment'),
        path('comment/<int:id>/approve/<str:tittle>/', views.comment_approve, name='comment_approve'),
        path('comment/<int:id>/remove/<str:tittle>/', views.comment_remove, name='comment_remove'),
        path('custom_article/', views.custom_article, name='custom_article'),
        path('about/', views.about, name='about'),
        path('contact/', views.contact, name='contact'),
        path('register_admin/', views.register_admin,name='register_admin'),
        path('register/', views.register_user,name='register'),
        path('register_author/', views.register_author,name='register_author'),
        path('login/', views.login_user,name='login'),
        path('logout/', views.logout_view,name='logout'),
        path('mumbai/', views.mumbai_view,name='mumbai'),
        path('goa/', views.goa_view,name='goa'),
        path('delhi/', views.delhi_view,name='delhi'),
        path('hyderabad/', views.hyderabad_view, name='hyderbabad'),
    ]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
