from django.shortcuts import render

API_KEY = "cf0e15e86eadac600fb90816161bc918-acb0b40c-ded5c319"


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


# def send_simple_message():
# 	return requests.post(
# 		"https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
# 		auth=("api", "YOUR_API_KEY"),
# 		data={"from": "Excited User <mailgun@YOUR_DOMAIN_NAME>",
# 			"to": ["bar@example.com", "YOU@YOUR_DOMAIN_NAME"],
# 			"subject": "Hello",
# 			"text": "Testing some Mailgun awesomness!"})

def send_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox6c4b3a7aaf8f491eb42d2ba65f011c33.mailgun.org/messages",
        auth=("api", API_KEY),
        data={"from": "Excited User <mailgun@YOUR_DOMAIN_NAME>",
              "to": ["anthony.sifontes@gmail.com", "anthony.sifontes@gmail.com"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})


def send_email(request):
    email = request.POST['email']
    message = "Thank you for subscribing!"

    send_message()
    return redirect('/')
