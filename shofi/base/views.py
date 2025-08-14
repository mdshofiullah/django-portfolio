from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .forms import PostForm
from .filters import PostFilter
from .models import Post, Skill, PricingPlan, Testimonial, ContactInfo, SocialLink, Service

def home(request):
    posts = Post.objects.filter(activate=True, featured=True).order_by('-created')[:3]
    skills = Skill.objects.all()
    pricing_plans = PricingPlan.objects.all()
    testimonials = Testimonial.objects.all()
    contact_info = ContactInfo.objects.first()
    social_links = SocialLink.objects.all()
    services = Service.objects.all()
    
    # Default contact info if not in database
    if not contact_info:
        contact_info = {
            'location': 'New York, NY, USA',
            'email': 'hello@shofi.dev',
            'phone': '+1 (555) 123-4567'
        }
    
    context = {
        'posts': posts,
        'skills': skills,
        'pricing_plans': pricing_plans,
        'projects': Post.objects.filter(activate=True).order_by('-created')[:3],
        'testimonials': testimonials,
        'contact_info': contact_info,
        'social_links': social_links,
        'services': services,
        'donation_link': "https://buymeacoffee.com/shofiullah",
    }
    return render(request, 'base/index.html', context)

def posts(request):
    post_list = Post.objects.filter(activate=True).order_by('-created')
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
    post = get_object_or_404(Post, slug=slug)
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

@csrf_exempt
def sendEmail(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from request body
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            subject = data.get('subject')
            message = data.get('message')
            
            # Basic validation
            if not all([name, email, subject, message]):
                return JsonResponse({'success': False, 'message': 'All fields are required'})
            
            # Create and save the email message to database
            from .models import EmailMessage
            email_message = EmailMessage(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            email_message.save()
            
            # Send the email
            template = render_to_string('base/email_template.html', {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message,
            })

            email = EmailMessage(
                subject,
                template,
                settings.EMAIL_HOST_USER,
                [settings.CONTACT_EMAIL]
            )
            email.fail_silently = False
            email.send()

            return JsonResponse({'success': True, 'message': 'Thank you for your message! I will get back to you soon.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'An error occurred: {str(e)}'})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)