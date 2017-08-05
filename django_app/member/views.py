from django.contrib.auth import login as django_login, \
    logout as django_logout
from django.shortcuts import render, redirect

# Create your views here.
from member.forms.login import LoginForm
from member.forms.signup import SignupForm


def login(request):
    print(request)

    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            user = form.cleaned_data['user']
            django_login(request, user)
            return redirect('') # postlist 로 보내고
    else:
        if request.user.is_authenticated:
            return redirect('') # postlist 로 보내고
    form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, '', context) # login 페이지로 보내고


def logout(request):
    django_logout(request)
    return redirect('') # 메인 페이지로 보내고


def signup(request):
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            user = form.create_user()
            django_login(request, user)
            return redirect('') # 메인 페이지로 보내고
    else:
        form = SignupForm()
    context = {
        'form': form,
    }
    return render(request, '', context) # signup 을 보내고
