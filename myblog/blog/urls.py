from django.urls import path
from . import views

urlpatterns = [
    path('',views.PostListView.as_view(),name='post_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
    path('post/new/',views.PostCreateView.as_view(),name='post_create'),
    path('post/<int:pk>/update/',views.PostUpdateView.as_view(),name='post_update'),
    path('draft/',views.PostDraftView.as_view(),name='post_draft_list'),
    path('post/<int:pk>/delete/',views.PostDeleteView.as_view(),name='post_confirm_delete'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/comment/', views.add_comments, name='add_comment'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]
