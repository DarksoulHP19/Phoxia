from django.urls import path
from . import views


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
]
