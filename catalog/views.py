from .models import Book, Location

from django.views import generic
from django.views.generic.edit import CreateView

from catalog.forms import (SignUpForm,EditProfileForm)
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# Home (index) view
def index(request):
    # search bar
    # most viewed book
    # most viewed location

    return render(
        request,
        'index.html',
        context={}
    )

# Book related -----------------------------------------------
class BookListView(generic.ListView):

    model = Book
    paginate_by = 10


# Will get all records from the db for the 'Book' model
class BookDetailView(generic.DetailView):
    model = Book


class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    template_name_suffix = '_add'
    fields = '__all__'


# Location related ----------------------------------------
class LocationListView(generic.ListView):
    model = Location
    paginate_by = 10


class LocationDetailView(generic.DetailView):
    model = Location


class LocationCreate(LoginRequiredMixin, CreateView):
    model = Location
    template_name_suffix = '_add'
    fields = '__all__'


# User related ----------------------------------------
def signup(request):
    # POST in HTTP basically means that the user is sending data as opposed to receiving it
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = SignUpForm()

        args = {'form':form}

        return render(request, 'accounts/signup.html', args)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/myprofile')
        else:
            return redirect('change-password')

    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)


# Contribution page to choose what to contribute
@login_required
def contribute(request):

    return render(
        request,
        'accounts/contribute.html',
        context={}
    )

