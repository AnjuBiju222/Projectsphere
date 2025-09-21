from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('userType')
        
        new_user = User(username=username, email=email, password=password, user_type=user_type)
        new_user.save()
        messages.success(request, 'Account created successfully!')
        return redirect('signup')  # Redirect to the signup page or any other page
        
    return render(request, 'signup.html')
