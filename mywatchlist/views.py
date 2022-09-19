from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers
# Belom diubah
# Create your views here.

def summary(watched):
    done = 0
    not_yet = 0
    for film in watched:
        if film.watched == "Yes":
            done +=1
        elif film.watched == "No":
            not_yet += 1
    
    if done >= not_yet:
        return "Selamat, kamu sudah banyak menonton!"
    else:
        return "Wah, kamu masih sedikit menonton!"
            

def show_watch_list(request):
    data_watch_list = MyWatchList.objects.all()
    kesimpulan = summary(data_watch_list)
    context = {
    'list_film': data_watch_list,
    'nama': 'Fajar Rivaldi Ibnusina',
    'studentID': '2106707050',
    'summary' : kesimpulan,
    }   
    return render(request, "watchlist.html" ,context)

def home(request):
    return render(request, "home.html")

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request,id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request,id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")