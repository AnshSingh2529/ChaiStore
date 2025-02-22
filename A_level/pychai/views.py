from django.shortcuts import render
from .models import ChaiVariety, Store
from django.shortcuts import redirect, get_object_or_404
from .forms import PyChaiForm, StoreForm

# Listing of views here using the models and forms.
def all_pychai(request):
    chais = ChaiVariety.objects.all().order_by('-date_added')
    return render(request, 'pychai/all_pychai.html', {'chais': chais})

def pychai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, 'pychai/pychai_detail.html', {'chai': chai})

def pychai_store(request):
    stores = Store.objects.all()
    return render(request, 'pychai/pychai_store.html', {'stores': stores}) # jinja2 template to be used here.



# Creation of New Chai or Store using forms.
def add_pychai(request):
    if request.method == 'POST':
        form = PyChaiForm(request.POST, request.FILES)
        if form.is_valid():
            chai = form.save(commit=False)
            chai.user = request.user
            chai.save()
            return redirect('all_pychai')
    else:
        form = PyChaiForm()
    return render(request, 'pychai/create_pychai_form.html', {'form': form}) 

def edit_pychai(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id, user=request.user)
    if request.method == 'POST':
        form = PyChaiForm(request.POST, request.FILES, instance=chai)
        if form.is_valid():
            form.save()
            return redirect('all_pychai')
    else:
        form = PyChaiForm(instance=chai)
    return render(request, 'pychai/create_pychai_form.html', {'form': form})   # jinja2 template to be used here.

def delete_pychai(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id, user=request.user)
    if request.method == 'POST':
        chai.delete()
        return redirect('all_pychai')
    return render(request, 'pychai/delete_pychai_confirm.html', {'chai': chai}) # jinja2 template to be used here.

def create_store(request):
    if request.method == 'POST':
        form = StoreForm(request.POST,request.FILES)
        if form.is_valid():
            store = form .save(commit=False)
            store.Store_owner = request.user
            store.save()
            return redirect('pychai_store')
    else:
        form = StoreForm()
    return render(request, 'pychai/create_store_form.html', {'form': form}) # jinja2 template to be used here.

def edit_store(request, store_id):
    store = get_object_or_404(Store, pk=store_id, Store_owner=request.user)
    if request.method == 'POST':
        form = StoreForm(request.POST, request.FILES, instance=store)
        if form.is_valid():
            form.save()
            return redirect('pychai_store')
    else:
        form = StoreForm(instance=store)
    return render(request, 'pychai/create_store_form.html', {'form': form}) # jinja2 template to be used here.

def delete_store(request, store_id):
    store = get_object_or_404(Store, pk=store_id, Store_owner=request.user)
    if request.method == 'POST':
        store.delete()
        return redirect('pychai_store')
    return render(request, 'pychai/delete_store_confirm.html', {'store': store}) # jinja2 template to be used here.



