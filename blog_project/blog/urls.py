from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('category/<int:category_id>/', views.category_posts, name='category_posts'),
    path('subscribe/<int:category_id>/', views.subscribe_category, name='subscribe_category'),
    path('unsubscribe/<int:category_id>/', views.unsubscribe_category, name='unsubscribe_category'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
    path('post/<int:post_id>/dislike/', views.dislike_post, name='dislike_post'),
    path('add-post/', views.add_post, name='add_post'),

]
