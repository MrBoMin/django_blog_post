from django.shortcuts import render,redirect
from .forms import RegisterForm, LoginForm,PostForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from .models import Post

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user 
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/index.html', {'form':form, 'posts':posts}) 

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print("Form is valided")
            form.save() 
            return redirect('login')
        else:
            print(form.errors)

    else:
        form = RegisterForm()

    return render(request, 'blog/register.html', {'form' :form})



def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                django_login(request, user)  # Use Django's login function
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
        else:
            # Handle form validation errors (optional)
            pass
    else:
        form = LoginForm()

    return render(request, 'blog/login.html', {'form': form})



def check_session(request): 
    if request.user.is_authenticated:
        session_key = request.session.session_key
        user_id = request.session.get('_auth_user_id')
        return render(request, 'blog/test.html', {'session_key': session_key, 'user_id': user_id})
    else:
        return redirect('login')
    

def logout(request):
    django_logout(request)
    return redirect('login')


def post_detail(request, id):
    post = Post.objects.filter(id=id).get() 
    if not post:
        return redirect('home')
    return render(request, 'blog/post.html', {'post' : post})


