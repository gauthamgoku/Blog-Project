from django.shortcuts import render, redirect ,HttpResponse
from django.urls import reverse
from django.contrib.auth import views as auth_views
from .models import Articles , Register , Article_Comment ,Register_Author
from django.core.files import File
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import UserLoginForm, UserCreationForm , LoginForm ,Register_User
from django.contrib.auth.models import User ,AnonymousUser
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_list_or_404, get_object_or_404


def base(request):
    article_fetch = Articles.objects.order_by('-post_time')
    return render(request, 'blog/home.html', {'article_fetch':article_fetch})


def about(request):
    context = {}
    return render(request, 'blog/about.html', context)


def contact(request):
    context = {}
    return render(request, 'blog/contact.html', context)


def goa_view(request):
    context = {}
    return render(request, 'blog/goa.html', context)


def mumbai_view(request):
    context = {}
    return render(request, 'blog/mumbai.html', context)


def delhi_view(request):
    context = {}
    return render(request, 'blog/delhi.html', context)

def hyderabad_view(request):
    context = {}
    return render(request, 'blog/hyderabad.html', context)

def newest_comment(request,tittle):
    article_comment = Article_Comment.objects.all().order_by('-comment_time')
    article_fetch = Articles.objects.filter(tittle=tittle)
    for art in article_fetch:
     print(art.tittle,'tittle')
    return render(request,'blog/detail_article.html', {'article_fetch':article_fetch , 'article_comment':article_comment})


def oldest_comment(request,tittle):
    article_comment = Article_Comment.objects.all()
    article_fetch = Articles.objects.filter(tittle=tittle)
    return render(request, 'blog/detail_article.html',{'article_fetch': article_fetch, 'article_comment': article_comment})


def detail_article(request , tittle ):

    article_fetch = Articles.objects.filter(tittle=tittle)
    article_comment = Article_Comment.objects.all()
    return render(request, 'blog/detail_article.html', {'article_fetch':article_fetch , 'article_comment':article_comment})

def delete_article(request , id ):

    
    Articles.objects.filter(id=id).delete()
    article_fetch = Articles.objects.order_by('-post_time')
    return render(request, 'blog/article_display.html', {'article_fetch':article_fetch})


def edit_article(request , id ):
    if request.method == "POST":
        title = request.POST.get('title')
        article = request.POST.get('article')
        image = request.FILES.get('article_image','')
        article_db = Articles.objects.get(id=id)
        article_db.tittle=title
        article_db.article=article
        article_db.image=image
        article_db.user = request.user
        article_db.save()
        return redirect('/articles/')

    article_fetch = Articles.objects.filter(id=id)
    return render(request, 'blog/article_edit.html', {'article_fetch':article_fetch})


def comments(request):
    if request.method == "POST":
        tittle = request.POST.get('tittle')
        article_comment = request.POST.get('comment')
        username = request.POST.get('username')
        if username == '':
            comment_db = Article_Comment(tittle=tittle,username=username,article_comment=article_comment)
            comment_db.save()
        else:
            approved_comment = True
            comment_db = Article_Comment(tittle=tittle, username=username, article_comment=article_comment , approved_comment=approved_comment)
            comment_db.save()
        return redirect('/articles/'+tittle+'/')

    else:
        return render(request, 'blog/detail_article.html', {})

@login_required
def comment_approve(request,tittle, id):
    print (tittle,id,"detail")
    comment = get_object_or_404(Article_Comment, id=id)
    comment.approve()
    return redirect('/articles/'+tittle+'/', id=comment.id)

@login_required
def comment_remove(request,tittle, id):
    comment = get_object_or_404(Article_Comment, id=id)
    comment.delete()
    return redirect('/articles/'+tittle+'/', id=comment.id)




def articles(request):

    article_fetch = Articles.objects.order_by('-post_time')
    return render(request, 'blog/article_display.html', {'article_fetch':article_fetch})

def newest_articles(request):
    article_fetch = Articles.objects.all().order_by('-post_time')
    return render(request, 'blog/article_display.html', {'article_fetch': article_fetch})


def oldest_articles(request):
    article_fetch = Articles.objects.all()
    return render(request, 'blog/article_display.html', {'article_fetch': article_fetch})


@login_required(login_url='/')
def custom_article(request):
    if request.method == "POST":
        title = request.POST.get('title')
        article = request.POST.get('article')
        image = request.FILES.get('article_image','')
        article_db = Articles(tittle=title, article=article , image=image)
        article_db.user = request.user
        article_db.save()
        return redirect('/articles/')

    article_fetch = Articles.objects.all()
    return render(request, 'blog/article_new.html', {'article_fetch':article_fetch})


def register_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        form_obj = User.objects.create_superuser(username=username, email=email,password=password)
        form_obj.save()

        return redirect('/login/')
    else:
        form = User()
        return render(request,'blog/register_admin.html',{'form' :form ,})



def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        form_obj = User.objects.create_user(username=username, email=email,password=password)
        form_obj.save()

        return redirect('/login/')
    else:
        form = User()

    return render(request,'blog/register.html',{'form' :form ,})


def register_author(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        form_obj = Register_Author.objects.create(username=username, email=email,password=password)
        form_obj.save()

        return redirect('/login/')
    else:
        form = Register_Author()

    return render(request,'blog/register_author.html',{'form' :form ,})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password , "username user")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('Invalid Credientials', status=401)
    else:


        reister_fetch = User.objects.all()
        for rf in reister_fetch:
            print(rf.username , "rf")
            print(rf.password , "pass")
        return render(request, 'blog/login.html', {'reister_fetch': reister_fetch});

       



def logout_view(request):
    logout(request)
    return redirect('/')
