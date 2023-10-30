from django.urls import path
from . import views

urlpatterns = [
    path('comments_list/', views.comments_list, name='comments_list'),
    path('create_comment/', views.create_comment, name='create_comment'),
    path('update_comment/<int:comment_id>/', views.update_comment, name='update_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
