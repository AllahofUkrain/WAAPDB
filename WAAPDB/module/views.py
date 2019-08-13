from django.shortcuts import render, reverse, HttpResponseRedirect
import psycopg2

# Create your views here.
def index(request):
    conn = psycopg2.connect(dbname='gis', user='postgres',
                            password='1', host='localhost', port='5432')
    cur = conn.cursor()
    if request.method == 'POST' and "sign_in" in request.POST:
        return HttpResponseRedirect('authorization')
    return render(request, 'index.html')


def work(request):
    return render(request, 'work.html')


def sign_in(request):
    if request.method == 'POST' and "sign_in" in request.POST:
        return HttpResponseRedirect('work')
    return render(request, 'sign_in.html')