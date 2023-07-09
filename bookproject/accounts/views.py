from django.contrib.auth import login
from django.shortcuts import render, redirect
from bookproject.backends import CustomAuthenticationBackend
from .forms import SignUpForm, CustomAuthenticationForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user.set_password(raw_password)
            user.save()

            user = CustomAuthenticationBackend().authenticate(request, username=email, password=raw_password)
            if user is not None:
                user.backend = 'bookproject.backends.CustomAuthenticationBackend'
                login(request, user)
                return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            user = CustomAuthenticationBackend().authenticate(request, username=email, password=raw_password)
            if user is not None:
                user.backend = 'bookproject.backends.CustomAuthenticationBackend'
                login(request, user)
                return redirect('index')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
