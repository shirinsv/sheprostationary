from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Products
from . formfile import product_form
# Create your views here.
def index(request):
    product=Products.objects.all()
    context={
        'product_list':product
    }
    return render(request,"index.html",context)
def detail(request,product_id):
    product=Products.objects.get(id=product_id)
    return render(request,"detail.html",{'product':product})

def add_products(request):
    if request.method=="POST":
        name=request.POST.get('name', )
        description=request.POST.get('description', )
        price=request.POST.get('price',)
        image=request.FILES['image']
        product=Products(name=name,description=description,price=price,image=image)
        product.save()
    return render(request,'add.html')

def update(request,id):
    product=Products.objects.get(id=id)
    form=product_form(request.POST or None,request.FILES,instance=product)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'product':product})

def delete(request,id):
    if request.method == "POST":
        product=Products.objects.get(id=id)
        product.delete()
        return redirect('/')
    return render(request,'delete.html')
