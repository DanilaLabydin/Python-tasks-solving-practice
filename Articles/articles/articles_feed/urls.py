from django.urls import path, re_path
from .views import *
urlpatterns = [
    path('', ArticlesHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add_article/', AddArticle.as_view(), name='add_article'),
    path('contacts/', contacts, name='contacts'),
    path('login/', login, name='login'),
    path('article/<slug:article_slug>/', ShowArticle.as_view(), name='article'),
    path('category/<slug:cat_slug>/', ArticleCategory.as_view(), name='category'),
    path('register/', RegisterUser.as_view(), name='register'),

]
#path('category/<int:cat_id>/', show_category, name='category')