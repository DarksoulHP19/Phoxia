from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect
from  .models import Profile,Post
from django.contrib.auth import authenticate,login ,logout
from django.db.models import Q
# Create your views here.
def index(request):
    posts = Post.objects.filter(Q(profile__followers=request.user) & ~Q(likes=request.user))
    context = {"posts":posts}
    return render(request,'Index.html',context)


def Login(request):
     if request.method == 'POST':
        username = request.POST ['username']
        password = request.POST ['password']
        user = authenticate(username=username,password=password)
        if user : 
            login(request,user)
            return redirect("profile")    
     return render(request,'Login.html')

def create_profile(request):
    if request.method == 'POST':
        username = request.POST ['username']
        password = request.POST ['password']
        image = request.FILES ['image']
        user = User.objects.create_user(username=username,password=password)
        profile = Profile.objects.create(user=user , profile_picture = image)
        
        if profile:
            messages.success(request,'profile creted please login')
            return redirect("Login")
        
    return render(request,'Signup.html')

#for rendering the profile page
def profile(request):
    profile =Profile.objects.get(user=request.user)
    posts = Post.objects.filter(user=request.user)
    posts_num = posts.count()
    return render(request,'profile.html',{'profile':profile , 'profile_user' : True,'posts':posts,'posts_num':posts_num})


def Logout(request):
    logout(request)
    return redirect("Login")

def search(request):
    search = request.GET['username']
    profiles =Profile.objects.filter(user__username__icontains=search)
    context = {'profiles':profiles, 'username':search}
    return render(request,'search.html',context)

def follow(request,id,username):
    profile = Profile.objects.get(id =id)
    login_profile = Profile.objects.get(user=request.user)
    if request.user in profile.followers.all():
         profile.followers.remove(request.user)
         login_profile.followings.remove(profile.user)
    else:
         profile.followers.add(request.user)
         login_profile.followings.add(profile.user)
    return redirect(f'search/?username={username}')

def upload_post(request):
    if request.method == 'POST':
        post = request.FILES['post']
        profile = Profile.objects.get(user=request.user)
        posts = Post.objects.create(user=request.user,Wallpaper=post,profile=profile)
        if posts:
            messages.success(request,'post uploaded')
    return render(request,'uploadposts.html')


def like_post(request,id):
    post = Post.objects.filter(id=id)
    if request.user in post[0].likes.all():
        post[0].likes.remove(request.user)
    else:
        post[0].likes.add(request.user)
    return redirect("index")
    