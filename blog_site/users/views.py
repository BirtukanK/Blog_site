from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created! You can login now')
            return redirect('blog-in')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@require_POST
def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')

def logout_done(request):
    return render(request, 'users/logout.html')

@login_required
def profile(request):
    return render(request, 'users/profile.html')