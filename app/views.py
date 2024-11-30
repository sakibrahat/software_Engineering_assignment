from django.shortcuts import render, redirect, get_object_or_404
from app.models import Item
from app.viewmodels import ItemViewModel

def item_list(request):
    items = ItemViewModel.get_all_items()
    return render(request, 'item_list.html', {'items': items})

def item_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        Item.objects.create(name=name, description=description)
        return redirect('item_list')
    return render(request, 'item_form.html')

def item_update(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        item.name = request.POST.get('name')
        item.description = request.POST.get('description')
        item.save()
        return redirect('item_list')
    return render(request, 'item_form.html', {'item': ItemViewModel(item).to_dict()})

def item_delete(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('item_list')
