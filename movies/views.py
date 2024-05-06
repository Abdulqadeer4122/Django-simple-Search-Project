from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie
from django.db.models import Q


# Create your views here.

def index(request):
    movies = Movie.objects.all()
    return render(request, 'Index.html', {'movies': movies})


def detail(request, id):
    data = Movie.objects.get(id=id)
    return render(request, 'detail.html', {'data': data})


def home(request):
    return redirect(request, 'Index.html')


def search(request):
    if request.method == 'POST':
        query_data = request.POST.get('search', '')
        movies = Movie.objects.filter(Q(title__icontains=query_data) | Q(genre__name__icontains=query_data))
        return render(request, 'Index.html', {'movies': movies})
    return render(request, 'Index.html')
