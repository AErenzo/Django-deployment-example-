from django.shortcuts import render
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from AppTwo.models import Users, ProjectIdea
from AppTwo.forms import RegisterForm, ContactForm, SignUpForm, ProjectsForm, UserForm, UserProfileInfoForm

# Create your views here.


def index(request):
    my_dict = {'home': "Welcome to the home page!"}
    return render(request, 'AppTwo/index.html', my_dict)


def Help(request):
    my_dict = {'contact': "Get in contact!"}
    return render(request, 'AppTwo/help.html', context=my_dict)


def users(request):
    user_list = Users.objects.all()
    user_dict = {'Activate_Users': user_list}
    return render(request, 'AppTwo/users.html', context=user_dict)

def sign_up_modelform(request):

    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return users(request)
        else:
            print('Error: Invalid Form')

    return render(request, 'AppTwo/sign_up.html', {'form': form})


def submitted_projects(request):
    proj_list = ProjectIdea.objects.all()
    proj_dict = {'projects': proj_list}
    return render(request, 'AppTwo/submitted_projects.html', context=proj_dict)


def project_model_form(request):
    form = ProjectsForm

    if request.method == 'POST':
        form = ProjectsForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return submitted_projects(request)
        else:
            print('Invalid Form')

    return render(request, 'AppTwo/project_ideas.html', {'form': form})


# def project_idea_form(request):
#     form = ProjectIdeaForm
#
#     if request.method == 'POST':
#
#         form = ProjectIdeaForm(request.POST)
#
#         if form.is_valid():
#             print('Validation Success')
#             print('First Name: '+form.cleaned_data['First_Name'])
#             print('Last Name: '+form.cleaned_data['Last_Name'])
#             print('Email: '+form.cleaned_data['Email'])
#             print('Project Category: '+form.cleaned_data['Project_Category'])
#             print('Project Name: '+form.cleaned_data['Project_Name'])
#             print('Project Description: '+form.cleaned_data['Proj_Description'])
#
#     return render(request, 'AppTwo/project_ideas.html', {'form': form})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        # checks if the user variable above has authenticated
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('User Account not Active')
        else:
            print('Login failed - Username: {} and password: {}'.format(username, password))
            return HttpResponse('Invalid login - Please try again or register if you do not have an account')

    else:
        return render(request, 'AppTwo/login.html')

# decorator added - login_required ensures that the logout view only works if the user is logged in
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register_form(request):

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        user_profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and user_profile_form.is_valid():

            user = user_form.save()
    #    below hashes the submitted password
            user.set_password(user.password)
            user.save()

            profile = user_profile_form.save(commit=False)
            # below tell django that the userProfileInfoForm is part of the UserForm - create the 1TO1 relationship
            profile.user = user

            # This check if profile_pic is included in the request files, if so set profile_pic to = the profile_pic
            #                                                                                     from the request files
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, user_profile_form.errors)
    else:
        user_form = UserForm()
        user_profile_form = UserProfileInfoForm()

    return render(request, 'AppTwo/register.html', {'user_form': user_form,
                                                    'user_profile_form': user_profile_form,
                                                    'registered': registered})


def contact_form(request):
    form = ContactForm

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            raise forms.ValidationError('Error: Invalid inputs, please review the form')

    return render(request, 'AppTwo/contact.html', {'form': form})



