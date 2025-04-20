from django.views.generic import DetailView, CreateView
from django.shortcuts import render
from .models import Item


#FBV
def index_view(request):
    items = Item.objects.all().select_related('inventory').prefetch_related('tags')
    context = {
        'item_list': items
    }
    return render(request,'items/index.html', context)


#CBV
class ItemDetailView(DetailView):
    model = Item


class ItemCreateView(CreateView):
    model = Item
    fields = ('name', 'weight')
    success_url = '/'


# filter
#   Item.objects.filter(name='...')
#   Item.objects.filter(weight=100)
#   Item.objects.filter(weight__lt=100) if weight < 100
#   Item.objects.filter(name__contains='d') if 'd' in name
#   Item.objects.exclude(name__contains='d') if name not contains 'd'
#   Item.objects.filter(inventory__name__startswith='H')