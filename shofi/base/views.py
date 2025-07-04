from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from .forms import PostForm
from .filters import PostFilter
from .models import Post, Skill, PricingPlan, Testimonial, ContactInfo, SocialLink, Service


# def home(request):
#     posts = Post.objects.filter(activate=True, featured=True).order_by('-created')[:3]
#     return render(request, 'base/index.html', {'posts': posts})

def home(request):
    posts = Post.objects.filter(activate=True, featured=True).order_by('-created')[:3]
    skills = Skill.objects.all()
    pricing_plans = PricingPlan.objects.all()
    testimonials = Testimonial.objects.all()
    contact_info = ContactInfo.objects.first()
    social_links = SocialLink.objects.all()
    services = Service.objects.all()
    
    context = {
        'posts': posts,
        'skills': skills,
        'pricing_plans': pricing_plans,
        'projects': Post.objects.filter(activate=True).order_by('-created')[:3],  # Use Post as projects
        'testimonials': testimonials,
        'contact_info': contact_info,
        'social_links': social_links,
        'services': services,
        'donation_link': "https://buymeacoffee.com/shofiullah",
    }
    return render(request, 'base/index.html', context)

def posts(request):
    post_list = Post.objects.filter(activate=True).order_by('-created')  # ✅ ordering added
    myFilter = PostFilter(request.GET, queryset=post_list)
    filtered_posts = myFilter.qs

    page = request.GET.get('page')
    paginator = Paginator(filtered_posts, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {'posts': posts, 'myFilter': myFilter}
    return render(request, 'base/posts.html', context)


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)  # ✅ safer than .get()
    return render(request, 'base/post.html', {'post': post})


def profile(request):
    return render(request, 'base/profile.html')


@login_required(login_url="home")
def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts')
    return render(request, 'base/post_form.html', {'form': form})


@login_required(login_url="home")
def updatePost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
    return render(request, 'base/post_form.html', {'form': form})


@login_required(login_url="home")
def deletePost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        post.delete()
        return redirect('posts')
    return render(request, 'base/delete.html', {'item': post})


def sendEmail(request):
    if request.method == 'POST':
        template = render_to_string('base/email_template.html', {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['alsait.shofiullah@gmail.com'],
        )
        email.fail_silently = False
        email.send()

        return render(request, 'base/email_sent.html')

    return redirect('home')  # fallback if accessed via GET
