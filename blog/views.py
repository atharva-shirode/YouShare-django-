from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse

# Create your views here.
posts = [
    {
        'title' : 'Post 1',
        'author' : 'ADS',
        'content' : 'Messi is the best!',
        'date' : '29 February 2021'
    },

    {
        'title' : 'Post 2',
        'author' : 'LM10',
        'content' : 'Barca is the worst!',
        'date' : '30 February 2021'
    }

]
def home(request):
    connect={
        'post': posts
    }
    return render(request,'blog/home.html',connect)

def about(request):
    return render(request,'blog/about.html')

