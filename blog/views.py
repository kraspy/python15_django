from django.shortcuts import render
from .models import Post


# Create your views here.
def index(request):
    return render(
        request,
        'blog/index.html',
        {
            'page_title': 'Index page',
            'posts': Post.objects.all(),
        },
    )
