from django.shortcuts import render
from blog.models import Post
from promotions.models import Promotion
from django.utils import timezone

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:2]
    promotions = Promotion.objects.all()[:4]
    return render(request, 'index.html', {'posts': posts, 'promotions': promotions})

