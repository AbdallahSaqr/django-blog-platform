from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Post, Category, Tag, ForbiddenWord, Comment, Profile
from .forms import RegistrationForm, LoginForm, CommentForm, PostForm

# Create your views here.
def filter_forbidden_words(text):
    forbidden = ForbiddenWord.objects.values_list('word', flat=True)
    for word in forbidden:
        text = text.replace(word, '*' * len(word))
    return text

def landing(request):
    posts = Post.objects.order_by('-published')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = Category.objects.all()
    return render(request, 'blog/landing.html', {
        'page_obj': page_obj,
        'categories': categories,
    })

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'blog/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                if hasattr(user, 'profile') and user.profile.is_blocked:
                    messages.error(request, "Sorry you are blocked, contact the admin")
                    return redirect('login')
                login(request, user)
                return redirect('landing')
            else:
                messages.error(request, "Invalid credentials")
    else:
        form = LoginForm()
    return render(request, 'blog/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('landing')

@login_required
def subscribe_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.subscribers.add(request.user)
    send_mail(
        'Subscription Confirmation',
        f'Hello {request.user.username}, you have subscribed successfully in {category.name}. Welcome aboard!',
        'from@example.com',
        [request.user.email],
        fail_silently=False,
    )
    return redirect('landing')

@login_required
def unsubscribe_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.subscribers.remove(request.user)
    return redirect('landing')

def category_posts(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = category.posts.order_by('-published')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/category_posts.html', {
        'category': category,
        'page_obj': page_obj,
    })

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    form = CommentForm()
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.content = filter_forbidden_words(comment.content)
            comment.save()
            return redirect('post_detail', post_id=post.id)
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.likes.add(request.user)
    return redirect('post_detail', post_id=post_id)

@login_required
def dislike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.dislikes.add(request.user)
    if post.dislikes.count() > 10:
        post.delete()
        return redirect('landing')
    return redirect('post_detail', post_id=post_id)


@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import Category

@login_required
def subscribe_category(request, category_id):
    if request.method == 'POST':
        category = get_object_or_404(Category, id=category_id)
        category.subscribers.add(request.user)
    return redirect(request.META.get('HTTP_REFERER', 'landing'))

@login_required
def unsubscribe_category(request, category_id):
    if request.method == 'POST':
        category = get_object_or_404(Category, id=category_id)
        category.subscribers.remove(request.user)
    return redirect(request.META.get('HTTP_REFERER', 'landing'))

