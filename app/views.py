from django.shortcuts import render, HttpResponse, redirect

def index(request):

    return redirect('/shows')


def shows(request):
    return render(request,"index.html")


def new_show(request):
    pass


def create_show(request):
    pass


def show_id(request, id):
    pass


def show_edit(request, id):
    pass


def show_update(request, id):
    pass


def show_destroy(request, id):
    pass




