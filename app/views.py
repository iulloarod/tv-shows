from django.shortcuts import render, HttpResponse, redirect

def index(request):

    return redirect('/shows')


def shows(request):
    return render(request,"shows.html")


def new_show(request):
    return render(request,"new_show.html")


def create_show(request):
    pass


def show_id(request, id):
    return render(request,"tv_show.html")


def show_edit(request, id):
    pass


def show_update(request):
    return render(request,"edit_show.html")


def show_destroy(request, id):
    pass




