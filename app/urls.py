from django.urls import path 
from app.views import ArticleCreateView, ArticleListView, ArticleUpdateView, ArticleDeleteView

urlpatterns = [
    path("", ArticleListView.as_view(), name="home"),
    path("create/", ArticleCreateView.as_view(), name="create_article"),
    path("<int:pk>/update", ArticleUpdateView.as_view(), name="update_article"),
    path("<int:pk>/delete", ArticleDeleteView.as_view(), name="delete_article"),

]