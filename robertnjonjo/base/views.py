from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .decorators import *

from .forms import PostForm,CustomUserCreationForm,ProfileForm, ProjectForm,UserForm
from .filters import PostFilter,ProjectFilter

from .models import *

def home(request):
    posts = Post.objects.filter(active=True)
    projects =Project.objects.all()
    context = {'posts':posts,'projects':projects}
    return render(request,template_name='index.html',context=context)

def about(request):
    return render(request,template_name='about.html')

#def mywork(request):
    #return render(request,template_name='work.html')

#def blogs(request):
    return render(request,template_name='blog.html')

def blogs(request):
	posts = Post.objects.filter(active=True)
	myFilter = PostFilter(request.GET, queryset=posts)
	posts = myFilter.qs

	page = request.GET.get('page')

	paginator = Paginator(posts, 5)

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	context = {'posts':posts, 'myFilter':myFilter}
	return render(request, template_name='blog.html', context=context)

def projects(request):
    projects =Project.objects.all()
    context = {'projects':projects}
    return render(request,template_name='work.html',context=context)

def detail(request, slug):
	detail = Project.objects.get(slug=slug)

	if request.method == 'POST':
		Project.objects.create(
			title=request.title,
			detail=detail,
			body=request.POST['comment']
			)
		messages.success(request, "You're comment was successfuly posted!")

		return redirect('work', slug=detail.slug)


	context = {'detail':detail}
	return render(request, template_name='detail.html', context=context) 

def createProject(request):
	form = ProjectForm()

	if request.method == 'POST':
		form = ProjectForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect('work')

	context = {'form':form}
	return render(request, 'project_form.html', context=context)

def deleteProject(request, slug):
	project = Project.objects.get(slug=slug)

	if request.method == 'POST':
		project.delete()
		return redirect('work')
	context = {'item':project}
	return render(request, template_name='delete_project.html', context=context)

def updateProject(request, slug):
	project = Project.objects.get(slug=slug)
	form = ProjectForm(instance=project)

	if request.method == 'POST':
		form = ProjectForm(request.POST, request.FILES, instance=project)
		if form.is_valid():
			form.save()
		return redirect('work')

	context = {'form':form}
	return render(request, template_name='project_form.html', context=context)

def createPost(request):
	form = PostForm()

	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect('blog')

	context = {'form':form}
	return render(request, 'post_form.html', context=context)

def post(request, slug):
	post = Post.objects.get(slug=slug)

	if request.method == 'POST':
		PostComment.objects.create(
			author=request.user.profile,
			post=post,
			body=request.POST['comment']
			)
		messages.success(request, "You're comment was successfuly posted!")

		return redirect('blogs', slug=post.slug)


	context = {'post':post}
	return render(request, template_name='post.html', context=context)


    
def updatePost(request, slug):
	post = Post.objects.get(slug=slug)
	form = PostForm(instance=post)

	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			form.save()
		return redirect('blog')

	context = {'form':form}
	return render(request, template_name='post_form.html', context=context)

def deletePost(request, slug):
	post = Post.objects.get(slug=slug)

	if request.method == 'POST':
		post.delete()
		return redirect('blog')
	context = {'item':post}
	return render(request, template_name='delete.html', context=context)

def contact(request):
    return render(request,template_name='contact.html')


def registerPage(request):
	form = CustomUserCreationForm()
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.save()
			messages.success(request, 'Account successfuly created!')

			user = authenticate(request, username=user.username, password=request.POST['password1'])

			if user is not None:
				login(request, user)

			next_url = request.GET.get('next')
			if next_url == '' or next_url == None:
				next_url = 'home'
			return redirect(next_url)
		else:
			messages.error(request, 'An error has occured with registration')
	context = {'form':form}
	return render(request, template_name='register.html', context=context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')

	if request.method == 'POST':
		email = request.POST.get('email')
		password =request.POST.get('password')

		#Little Hack to work around re-building the usermodel
		try:
			user = User.objects.get(email=email)
			user = authenticate(request, username=user.username, password=password)
		except:
			messages.error(request, 'User with this email does not exists')
			return redirect('login')
			
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.error(request, 'Email OR password is incorrect')

	context = {}
	return render(request, template_name='login.html', context=context)

def registerPage(request):
	form = CustomUserCreationForm()
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.save()
			messages.success(request, 'Account successfuly created!')

			user = authenticate(request, username=user.username, password=request.POST['password1'])

			if user is not None:
				login(request, user)

			next_url = request.GET.get('next')
			if next_url == '' or next_url == None:
				next_url = 'home'
			return redirect(next_url)
		else:
			messages.error(request, 'An error has occured with registration')
	context = {'form':form}
	return render(request, template_name='register.html', context=context)

def logoutUser(request):
	logout(request)
	return redirect('home')

@login_required(login_url="home")
def userAccount(request):
	profile = request.user.profile

	context = {'profile':profile}
	return render(request, template_name='account.html', context=context)

@login_required(login_url="home")
def updateProfile(request):
	user = request.user
	profile = user.profile
	form = ProfileForm(instance=profile)
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=user)
		if user_form.is_valid():
			user_form.save()

		form = ProfileForm(request.POST, request.FILES, instance=profile)
		if form.is_valid():
			form.save()
			return redirect('account')


	context = {'form':form}
	return render(request, template_name='profile_form.html', context=context)   