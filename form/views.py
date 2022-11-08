from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, logout

from blog.models import Comment
from .forms import EnglishLevelForm, AuthenticationForm, RegistrationForm, ChangePasswordForm, CommentsFinderForm


def english_level(request):
    if request.method == 'POST':
        form = EnglishLevelForm(request.POST)
        if form.is_valid():
            return render(request, 'form/valid_form.html', {'data': form.cleaned_data})
    else:
        form = EnglishLevelForm()
    return render(request, 'form/english_level_form.html', {'form': form})


def authentication(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return HttpResponseRedirect('/form/user')
    else:
        form = AuthenticationForm()
    return render(request, 'form/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/form/login')


def user_page(request):
    return render(request, 'form/user.html')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            email=form.cleaned_data['email'],
                                            password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/form/user')
    else:
        form = RegistrationForm()
    return render(request, 'form/registration.html', {'form': form})


@login_required(login_url='/form/login')
def change_password(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST, user=user)
        if form.is_valid():
            user.set_password(form.cleaned_data['new_password'])
            user.save()
            login(request, user)
            return HttpResponseRedirect('/form/user')
    else:
        form = ChangePasswordForm(user=user)
    return render(request, 'form/change_password.html', {'form': form})


def comments_finder(request):
    form = CommentsFinderForm()
    if request.GET.get('comment') is not None:
        comment = request.GET.get('comment')
        if request.GET.get('author'):
            comments = Comment.objects.filter(author__nickname=request.user.username, body__icontains=comment)
        else:
            comments = Comment.objects.filter(body__icontains=comment)
        data = {
            'comments': comments,
            'form': form,
            'user': request.user,
        }
    else:
        data = {
            'form': form,
        }
    return render(request, 'form/comments_find.html', data)
