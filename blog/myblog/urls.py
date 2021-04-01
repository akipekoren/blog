
from django.urls import path
from .views import HomeView,DetailsView,AddPostView,EditPostView,DeletePostView,AddCategoryView,CategoryView,CategoryListView,LikeView

urlpatterns = [


path('', HomeView.as_view(), name="home"),
path('article/<int:pk>',DetailsView.as_view(), name='article-detail'),
path('add-post/', AddPostView.as_view(), name = 'add-post'),
path('article/edit/<int:pk>',EditPostView.as_view(), name = 'edit-post'),
path('article/<int:pk>/delete',DeletePostView.as_view(), name = 'delete-post'),
path('add-category', AddCategoryView.as_view(), name = 'add-category'),
path('category/<str:cats>', CategoryView, name='category'),
path('category-list/', CategoryListView, name='category-list'),
path('like/<int:pk>', LikeView, name="like-post"),


]
