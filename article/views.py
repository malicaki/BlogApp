from django.shortcuts import get_object_or_404, render, redirect

from article.models import Article
from .forms import ArticleForm
from django.contrib import messages


def index(request):
    return render(request,"index.html")
    
def about(request):
    return render(request,"about.html")

def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles":articles})
    articles = Article.objects.all()

    return render(request,"articles.html",{"articles":articles})

def updateArticle(request, slug):

    article = get_object_or_404(Article, slug=slug)
    form = ArticleForm(request.POST or None,request.FILES or None,instance = article)
    if form.is_valid():
        article = form.save(commit=False)
        
        article.author = request.user
        article.save()

        messages.success(request,"Makale başarıyla güncellendi")
        return redirect("article:dashboard")


    return render(request,"update.html",{"form":form})

def deleteArticle(request,slug):
    article = get_object_or_404(Article,slug=slug)

    article.delete()

    messages.success(request,"Makale Başarıyla Silindi")

    return redirect("article:dashboard")


def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles
    }
    return render(request,"dashboard.html",context)

def addArticle(request):

    form = ArticleForm(request.POST or None)

    if form.is_valid():
       article = form.save(commit=False)
       article.author = request.user
       article.save()
       messages.success(request,"Article Added")
       return redirect("article:dashboard")

    return render(request,"addarticle.html",{"form":form})

def detail(request,id):
    article = Article.objects.filter(id = id).first()   
    return render(request,"detail.html",{"article":article })
