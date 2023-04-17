from django.shortcuts import render
from .models import Item
from django.http import HttpResponse

def item_list(request):
    items = Item.objects.all()
    return render(request, 'items/item_list.html', {'items': items})


def index(request):
    return HttpResponse("Hello, world. You're at the items index.")
