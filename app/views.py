from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from  .models import Profile,Post
from django.contrib.auth import authenticate,login ,logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    context = {}
    
    if request.user.is_authenticated:
        # User is logged in - show posts and profile
        posts = Post.objects.filter(Q(profile__followers=request.user))
        profile = Profile.objects.get(user=request.user)
        context = {
            "posts": posts,
            "profile": profile,
            "profile_user": True
        }
    else:
        # User is not logged in - show promotional content only
        context = {
            "posts": [],
            "profile": None,
            "profile_user": False
        }
    
    return render(request, 'Index.html', context)

#for signup
def home_view(request):
    post = Post.objects.all().order_by('-id')[:6]  # Fetch the latest 6 posts
    context = {
        'posts': post,
    }
    return render(request, 'base.html', context)

#for login 
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect("index")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("Login")

    return render(request, 'Login.html')


#for create profile
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


#for logout
def Logout(request):
    logout(request)
    return redirect("Login")



#for search
def search(request):
    search = request.GET['username']
    profiles =Profile.objects.filter(user__username__icontains=search)
    context = {'profiles':profiles, 'username':search}
    return render(request,'search.html',context)


#for follow user
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


#for uploading post 
def upload_post(request):
    profile = Profile.objects.get(user=request.user)
    context = {
               "profile":profile,
               "profile_user":True}
    if request.method == 'POST':
        post = request.FILES['post']
        description = request.POST['description']
        profile = Profile.objects.get(user=request.user)
        posts = Post.objects.create(user=request.user,Wallpaper=post,profile=profile,description=description)
        if posts:
            messages.success(request,'post uploaded')
    return render(request,'uploadposts.html',context)


#for liking post
def like_post(request,id):
    post = Post.objects.filter(id=id)
    if request.user in post[0].likes.all():
        post[0].likes.remove(request.user)
    else:
        post[0].likes.add(request.user)
    return redirect("index")

#for commenting on post
# def  comment_post(request,id):
#     post = Post.objects.filter(id=id)
#     if request.method == 'POST':
#         comment = request.POST['comment']
#         post.comments = comment
#         post.save()
#         return render(request,'Comment.html')
#     return redirect("index")

#downloading the post
def download_post(request, id):
    post = get_object_or_404(Post, id=id)
    response = HttpResponse(post.Wallpaper, content_type='application/force-download')
    response ['Content-Disposition'] = f'attachment; filename="{post.Wallpaper.name}"'
    return response



#for subscription
# def subscription(request):
#     return render(request,'subscription.html')