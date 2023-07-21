from django.urls import path
from . import views

# urlpatterns = {
#     path(r'^$',views.PostListView.as_view(),name = 'post_list') ,
#     path(r'^about/$',views.AboutView.as_view(),name = 'about'),
#     path(r'post/(?P<pk>\d+)$', views.PostDetailView.as_view, name = 'post_detail') ,
#     path(r'post/new/$',views.CreatePostView.as_view, name = 'post_new'),
#     path(r'post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name = 'post_edit'),
#     path(r'^post/(?P<pk>\d+)/remove/$',views.PostDeleteView.as_view(), name = 'post_remove'),
#     path(r'^drafts/$',views.DraftListView.as_view(), name='post_draft_list'),
#     path(r'^post/(?<pk>\d+)/comment/$',views.add_comment_to_post,name='add_comment_to_post'),
#     path(r'^comment/(?<pk>\d+)/approve/$',views.comment_approve,name='comment_approve'),
#     path(r'^comment/(?<pk>\d+)/remove/$',views.comment_remove,name='comment_remove'),
#     path(r'^post/(?P<pk>\d+)/publish/$',views.post_publish,name='post_publish'),
# }
urlpatterns = [
    path('',views.PostListView.as_view(),name='post_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]
