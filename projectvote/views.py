from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render , get_object_or_404
from .forms import *
from django.contrib import messages
from django.urls import reverse
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate ,login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer

# Create your views here


def register(request):
    if request.method=='POST':
        form =newUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful")
            return redirect('userlogin')
        messages.error(request, 'Registration Failure')
    form=newUserForm()
    return render(request, 'register.html', {"register_form":form})

def userlogin(request):
    if request.method=='POST':
            form=AuthenticationForm(request,data=request.POST)
            if form.is_valid():
                username=form.cleaned_data.get('username')
                password=form.cleaned_data.get('password')
                user=authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, "Login Successful")
                    return redirect('index')
                else:
                    messages.error(request, "Invalid Username or Password")
            else:
                messages.error(request, "Invalid Username or Password")
    form=AuthenticationForm      
    return render(request, 'userlogin.html', {"form": form})

def projects(request):
    projects =Project.objects.all()
    return render(request, 'project.html', {"projects":projects})

@login_required(login_url='login')
def project_details(request, pk):
    project = Project.objects.get(pk=pk)
    user=request.user
    ratings=Rate.objects.filter(project=pk)
    count = 0
    design_rating_total=0
    content_rating_total=0
    usability_rating_total=0
    for rating in ratings:
       design_rating_total+=rating.designrate
       content_rating_total+=rating.contentrate
       usability_rating_total+=rating.usabilityrate
       count = count+1

    design_rating_avg = design_rating_total/count
    content_rating_avg = content_rating_total/count
    usability_rating_avg = usability_rating_total/count

    if request.method == 'POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            rate=form.save(commit=False)
            rate.user=user
            rate.project=project
            rate.save()
            return HttpResponseRedirect(reverse('project-details', args=(pk)))
    else:
        form=ReviewForm()
        project=project
    return render(request, 'project-details.html', {"project":project, "form": form, "design_rating_avg":design_rating_avg, "content_rating_avg":content_rating_avg, "usability_rating_avg":usability_rating_avg})

def main(request):
    projects = Project.objects.all()
    return render(request, 'index.html',{"projects":projects })

@login_required(login_url='login')
def post(request):
    projects = Project.objects.all()
    print(projects)
    users = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            project= form.save(commit = False)
            project.user = request.user
            project.save()
            messages.success(request, f'Successfully uploaded your pic!')
            return redirect('projects')
    else:
        form = PostForm()
    return render(request, 'post.html' ,{"projects":projects[::-1], "form": form, "users": users})

def rated(request, id):
    project=Project.objects.get(id=id)
    user=request.user
    if request.method == 'POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            rate=form.save(commit=False)
            rate.user=user
            rate.project=project
            rate.save()
            return HttpResponseRedirect(reverse('project-details', args=('project')))
    else:
        form=ReviewForm()
    return render(request,'rate.html',{"form": form})

# @login_required(login_url='login')
# def user_profile(request, username):
#     user_prof = get_object_or_404(User, username=username)
#     if request.user == user_prof:
#         return redirect('profile', username=request.user.username)
#     params = {
#         'user_prof': user_prof,
#     }
#     return render(request, 'userprofile.html', params)

def profile(request):
    user=request.user
    my_profile=Profile.objects.get(user=user)
    return render(request,"profile.html",{'my_profile':my_profile,"user":user})

@login_required(login_url='login')
def update_profile(request):
    
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('profile')

    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    contex = {
        'user_form': user_form,
        'prof_form': prof_form,

    }
    return render(request, 'update.html', contex)

@login_required(login_url='login')
def search_project(request):
    if request.method == 'GET':
        name = request.GET.get("title")
        results = Project.objects.filter(name__icontains=name).all()
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'search.html', params)
    else:
        message = "You haven't searched for any image category"
    return render(request, 'search.html', {'message': message})


def signout(request):
    logout(request)
    messages.success(request,"You have logged out successfuly")
    return redirect ('project')

class ProfileList(APIView):
    def get(self, request, format=None):
        profile = Profile.objects.all()
        serializers = ProfileSerializer(profile, many=True)
        return Response(serializers.data)

class ProjectList(APIView):
    def get(self, request, format=None):
        project = Project.objects.all()
        serializers = ProjectSerializer(project, many=True)
        return Response(serializers.data)