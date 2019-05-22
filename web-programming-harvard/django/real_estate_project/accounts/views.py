from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        # Login user
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect('login')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def register(request):
    if request.method == 'POST':
        # Register user
    else:
        return render(request, 'accounts/register.html')
