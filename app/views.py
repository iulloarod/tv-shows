from django.shortcuts import render, HttpResponse, redirect
from .models import Show
from time import strftime, localtime
import locale
locale.setlocale(locale.LC_ALL, 'es-ES')

def index(request):
    return redirect('/shows')


def shows(request):
    all_shows = Show.objects.all()
    if request.method == "GET":
        context= {
            "all_shows": all_shows,
        }
    return render(request,"shows.html", context)


def new_show(request):
    if request.method=='GET':
        return render(request,"new_show.html")


def create_show(request):
    if request.method=='POST':
        request.POST['title']
        request.POST['network']
        request.POST['release_date']
        request.POST['description']
        print(request.POST)
        Show.objects.create(title=request.POST['title'], 
                            network=request.POST['network'], 
                            rel_date=request.POST['release_date'],
                            desc= request.POST['description']
        )
        return redirect('/shows')


def show_id(request, id):
    return render(request,"tv_show.html")


def show_edit(request, id):
    pass
    return render(request,"edit_show.html")


def show_update(request, id):
    return redirect('/shows/<id>')


def show_destroy(request, id):
    pass
    return redirect('/shows')




