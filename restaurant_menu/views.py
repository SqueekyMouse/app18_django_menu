from django.shortcuts import render
from django.views import generic
from .models import Item

# Create your views here.
# gonna create class based view, cleaner approch!!!
class MenuList(generic.ListView): # for mail page!!
    queryset=Item.objects.order_by("-date_created")
    template_name="index.html"

class MenuItemDetail(generic.DetailView): # for item page!!
    model=Item
    template_name='menu_item_detail.html'