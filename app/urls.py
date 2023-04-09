from django.urls import path
from . import views
from .views import download_post

urlpatterns = [
    path('',views.index,name='index'),
    path('createprofile/', views.create_profile,name='signup'),
    path('login/',views.Login,name='Login'),
    path('logout/',views.Logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('search/',views.search ,name='search'),
    path('follow/<int:id>/<str:username>/',views.follow,name='follow'),
    path('uploadpost/',views.upload_post,name='upload_post'),
    path('like/<int:id>/',views.like_post,name='like'),
    path('download/<int:id>/download/',views.download_post, name='download_post'),
]
