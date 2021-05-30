from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, DeleteView
from .models import Item
from .forms import Item_Form


# Create your views here.
def items_index(request):
    items = Item.objects.all()
    return render(request, 'index.html', { 'items' : items })

class Create(CreateView):
    model = Item
    fields = '__all__'
    success_url = '/'

def items_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'index.html', {'item' : item })
    
class Delete(DeleteView):
  model = Item
  success_url = '/'

def showform(request):
    form = Item_Form(request.POST or None)

    if form.is_valid():
        form.save()
        context = {'form': form}
    return render(request, 'index.html', context)