from django.shortcuts import render

pages = ['Home', 'Bio', 'Blog', 'Projects']
pages = [
    {'title': 'Home',
    'file': '/'},
    {'title': 'Bio',
    'file': 'bio.html'},
    {'title': 'Blog',
    'file': 'blog.html'},
    {'title': 'Projects',
    'file': 'projects.html'}

]

# Create your views here.
def homepage(request):
    context = {
        'title': pages[0]['title'],
        'pages': pages,
    }

    return render(request, 'index.html', context)

def bio(request):
    context = {
        'title': pages[1]['title'],
        'pages': pages,
    }

    return render(request, 'bio.html', context)

def blog(request):
    context = {
        'title': pages[2]['title'],
        'pages': pages,
    }

    return render(request, 'blog.html', context)

def projects(request):
    context = {
        'title': pages[3]['title'],
        'pages': pages,
    }

    return render(request, 'projects.html', context)
