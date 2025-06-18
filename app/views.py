from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from .middlewares import auth, guest

from .models import DiaryEntry
from .forms import DiaryEntryForm

from newsapi import NewsApiClient

# Import Pagination Stuff

from django.core.paginator import Paginator
# Create your views here.

def home_view(request):
    return render(request,'home.html')

@guest
def register_view(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data={'username':'','password1':'','password2':''}
        form=UserCreationForm(initial=initial_data)
    return render(request, 'auth/register.html', {'form':form})

@guest
def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data={'username':'','password':''}
        form=AuthenticationForm(initial=initial_data)
    return render(request, 'auth/login.html', {'form':form})

@auth
def dashboard_view(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def diary_view(request):
    entries=DiaryEntry.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'diary.html',{'entries': entries})

def index_view(request):
    if request.method=='POST':
        form=DiaryEntryForm(request.POST)
        if form.is_valid():
            diary_entry=form.save(commit=False)
            diary_entry.user=request.user
            diary_entry.save()
            # form.save()
            return redirect('diary')
    else:
        form=DiaryEntryForm()
    return render(request, 'index.html',{'form':form})

def update_entry(request,pk):
    entry=get_object_or_404(DiaryEntry,pk=pk)
    if request.method == 'POST':
        form=DiaryEntryForm(request.POST,instance=entry)
        if form.is_valid():
            form.save()
            return redirect('diary')
    else:
        form=DiaryEntryForm(instance=entry)
    return render(request,'update_entry.html' , {'form':form})

def delete_entry(request, pk):
    entry=get_object_or_404(DiaryEntry,pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('diary')
    return render(request, 'delete_entry.html', {'entry': entry})

def entry_detail(request,pk):
    entry=get_object_or_404(DiaryEntry,pk=pk)
    return render(request, 'entry_detail.html', {'entry': entry})

def news_index(request):
    newsApi= NewsApiClient(api_key='34eff59231f8493581a00fee309d1eca')

    sources = 'bbc-news,cnn,techcrunch'
    headlines=newsApi.get_top_headlines(sources=sources)
    articles=headlines['articles']
    desc=[]
    news=[]
    img=[]
    links=[]

    for i in range(len(articles)):
        article=articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        links.append(article['url'])
    mylist = list(zip(news,desc,img,links))

    p=Paginator(mylist,5)
    page=request.GET.get('page')
    news_list=p.get_page(page)

    return render(request, "news.html",context={"mylist":mylist, "news_list":news_list})