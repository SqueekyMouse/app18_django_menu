from typing import Any, Dict
from django.shortcuts import render
from django.views import generic
from .models import Item

# Create your views here.
# gonna create class based view, cleaner approch!!!
class MenuList(generic.ListView): # for mail page!!
    queryset=Item.objects.order_by("-date_created")
    template_name="index.html"

    # context- key concept in django, to connect python data to html!!!
    def get_context_data(self) -> Dict[str, Any]:
        context={'meals': ['Pizza', 'Pasta'],
                 'ingredients':['things']}
        return(context)

class MenuItemDetail(generic.DetailView): # for item page!!
    model=Item
    template_name='menu_item_detail.html'