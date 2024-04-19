from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,UserLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from .models import *

def register(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
            user.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in {username}!')
            new=Doctor(name=request.POST['username'],email=request.POST['email'],username=user)
            new.save()
            return redirect('doc-login')
    else:
        form=UserRegisterForm()
    return render(request,'doctor/register.html',{'form':form})

@login_required
def dashboard(request):
    return render(request,'doctor/dashboard.html')

def doctorlogin(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user_authen = authenticate(request, username=username, password=password)
            if user_authen is not None:
                try:
                    doctor_data = Doctor.objects.get(username=user_authen)
                    print(doctor_data)
                    print("Doctor data found")
            
            # If patient data exists, log in the user and redirect to 'patprofile'
                    login(request, user_authen)
                    request.session['key'] = 'D'
                    return redirect('minor-home')
        
                except Doctor.DoesNotExist:
            # If patient data does not exist, redirect to 'minor-home'
                    print("The Doctor data does not exist")
                    form.add_error(None, 'Invalid username and password')
                    # Clear both fields
                    form.fields['username'].widget.attrs['value'] = ''
                    form.fields['password'].widget.attrs['value'] = ''
	 			

                
            else:
                # Check if both username and password are incorrect
                if not User.objects.filter(username=username).exists():
                    # Both username and password are incorrect
                    form.add_error(None, 'Invalid username and password')
                    # Clear both fields
                    form.fields['username'].widget.attrs['value'] = ''
                    form.fields['password'].widget.attrs['value'] = ''
                else:
                    # Username is valid, password is incorrect
                    form.add_error('password', 'Incorrect password')
                    # Clear only the password field
                    form.fields['password'].widget.attrs['value'] = ''
        # If the form is invalid or authentication fails, render the login form with error message
        return render(request, 'doctor/login.html', {'form': form})
    else:
        # If it's a GET request, just render the login form
        form = UserLoginForm()
        return render(request, 'doctor/login.html', {'form': form})