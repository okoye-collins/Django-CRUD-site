from django import forms
from django.shortcuts import redirect, render
from food import models
from food.models import Item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list
    }
    return render(request, 'food/index.html', context)

# class listview
class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name= 'item_list'

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    return render(request, 'food/detail.html', {'item':item})

# class base detai view
class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'

def add_item(request):
    # item = Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect ('index')

    return render(request, 'food/item_form.html',  context={'form':form})

class CreateItem(CreateView):
    model = Item;
    fields = ['item_name', 'item_dec', 'item_price', 'item_image']
    template_name = 'food/item_form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)

def edit(request, item_id):
    item = Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None, instance=item)
    
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'food/item_form.html', {'form':form, 'item':item})

def delete(request,item_id):
    item = Item.objects.get(id=item_id)

    if request.method == 'POST':
        item.delete()
        return redirect('index')
    return render(request, 'food/delete.html', {'item':item})

