from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    """
    View function for the home page.
    Renders the home page template.
    """
    return render(request, 'home.html')


def register(request):
    """
    View function for user registration.
    If the user is authenticated, redirects to the home page.
    Handles the registration form, validates input, creates a new user, logs them in, and
    redirects them to the home page with a success message.
    If the form is invalid, shows error messages.
    """
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user to the database
            login(request, user)  # Log the user in immediately after registration
            messages.success(request, f'Account created successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Error in registration. Please correct the errors below.')
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    """
    View function for user login.
    If the user is authenticated, redirects to the home page.
    Handles the login form, validates the username and password, and authenticates the user.
    If successful, logs the user in and redirects them to the home page.
    If invalid credentials are provided, shows an error message.
    """
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    """
    View function for logging out the user.
    Logs out the user and redirects them to the home page with a logout success message.
    """
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')


@login_required
def profile(request):
    """
    View function for the user profile page.
    Only accessible to authenticated users.
    Renders the user's profile page.
    """
    return render(request, 'accounts/profile.html')
