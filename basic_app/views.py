from django.shortcuts import render
from . import forms

from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as login_lib, logout as logout_lib
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
def index(request):
    context_dict = {
        'text': 'this text is written in views.py line 8',
        'number': 100
    }
    return render(request, 'basic_app/index.html', context_dict)


def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation Passed: \n")
            print("name: ", form.cleaned_data['name'])
            print("email: ", form.cleaned_data['email'])
            print("text: ", form.cleaned_data['text'])

    return render(request, 'basic_app/form_page.html', {'form': form})


# def about(req):
#     return render(req, 'basic_app/about.html')

# def base(req):
#     return render(req, 'basic_app/base.html')


def register(req):
    registered = False
    if req.method == "POST":
        user_form = forms.UserForm(data=req.POST)
        profile_form = forms.UserProfileInfoForm(data=req.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in req.FILES:
                profile.profile_pic = req.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()

    return render(
        req, 'basic_app/register.html', {
            'user_form': user_form,
            'profile_form': profile_form,
            'registered': registered
        })


def login(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login_lib(req, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("account not active")

        else:
            print('login failed')
            print('username: {} || password: {}'.format(username, password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(req, 'basic_app/login.html', {})


@login_required
def logout(req):
    logout_lib(req)
    return HttpResponseRedirect(reverse('index'))