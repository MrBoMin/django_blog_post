from django.shortcuts import render,redirect
from .forms import RegisterForm, LoginForm
# Create your views here.
def home(request):
    return render(request, 'blog/index.html') 

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
            form.save() 
            return redirect('home')
    else:
        form = LoginForm() 
    
    return render(request, 'blog/login.html', {'form' :form})