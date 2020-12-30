from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Movies, Series, Clips
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User



def index(request):
    movies = Movies.objects.all()
    paginator = Paginator(movies, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    #context = {'movies':movies}
    return render(request, 'index.html', context)

def series(request):
    series = Series.objects.all()
    context = {'series':series}
    return render(request, 'series.html', context)

def clips(request):
    clips = Clips.objects.all()
    paginator = Paginator(clips, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'clips.html', context)

def movie_detail(request, slug):
    #return HttpResponse(slug)
    single = Movies.objects.get(slug=slug)
    context = {'single':single}
    return render(request, 'moviedetails.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = RegisterForm()

    context = {'form':form}
    return render(request, 'registrations/register.html', context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            #login the user
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()

    context = {'form':form}
    return render(request, 'registrations/login.html', context)

def logout_view(request):
    #if request.method == 'POST':
    logout(request)
    return redirect('home')

def  user_edit_view(request):
    form = UserChangeForm()
    context = {'form':form}
    return render(request, 'registrations/enditprofile.html', context)

    def get_object(self):
        return self.request.user
