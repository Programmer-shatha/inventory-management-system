from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product ,Order
from .forms import ProductForm ,OrderForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

@login_required()
def index(request):
    orders=Order.objects.all()
    products=Product.objects.all()
    order_count=orders.count()
    product_count=products.count()
    customer_count=User.objects.all().count()
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.customer =request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form=OrderForm()
    context={
        'orders':orders,
        'form':form,
        'products':products,
        'order_count':order_count,
        'product_count':product_count,
        'customer_count':customer_count
    }
    return render(request,'dashboard/index.html',context)

@login_required()
def staff(request):
    customer =User.objects.all()
    customer_count=customer.count()
    product_count = Product.objects.all().count()
    order_count= Order.objects.all().count()
    context={
        'customer':customer,
        'customer_count':customer_count,
        'order_count':order_count,
        'product_count':product_count
    }
    return render(request,'dashboard/staff.html',context)

@login_required()
def staff_details(request,pk):
    customer=User.objects.get(id=pk)
    context={
        'customer':customer
    }
    return render(request,'dashboard/staff_details.html',context)

@login_required()
def product(request):
    items = Product.objects.all()
    product_count=items.count()
    customer_count=User.objects.all().count()
    order_count= Order.objects.all().count()
    if request.method =='POST':
        form =ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name=form.cleaned_data.get('name')
            messages.success(request,f'{product_name} has been added')
            return redirect('dashboard-product')
    else:
        form=ProductForm()
    
    context={
        'items':items,
        'form':form,
        'product_count':product_count,
        'customer_count':customer_count,
        'order_count':order_count
    }
    return render(request,'dashboard/product.html',context)

@login_required()
def product_delete(request ,pk):
    item =Product.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect ('dashboard-product')
    return render (request,'dashboard/product_delete.html',{'item':item})

@login_required()
def product_update(request ,pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request,'dashboard/product_update.html',context)


@login_required()
def order(request):
    orders= Order.objects.all()
    order_count= orders.count()
    customer_count=User.objects.all().count()
    product_count = Product.objects.all().count()
    context={
        'orders':orders,
        'customer_count':customer_count,
        'order_count':order_count,
        'product_count':product_count
    }
    return render(request,'dashboard/order.html',context)
