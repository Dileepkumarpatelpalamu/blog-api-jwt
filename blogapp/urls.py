from django.urls import path
from blogapp import views
urlpatterns = [
    path('viewallpost/',views.get_all_post,name="get_all_post"),
    path('addpost',views.add_post,name="add_post"),
    path('updatepost/<str:pk>',views.update_post,name="update_post"),
    path('deletepost/<str:pk>',views.delete_post,name="delete_post"),
]
