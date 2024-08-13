import os
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
# LogIn LogOut
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.

# LOGIN 
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username ,password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:  messages.info(request,'Tài Khoản Đăng Nhập Chưa Đúng..!')
    context={}
    return render(request,'app/login.html',context)

# LOGOUT
def logoutPage(request):
    logout(request)
    return redirect('viewhome')

# REGISTER
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context={'form':form}
    return render(request,'app/register.html',context)



def home(request):
    if request.user.is_authenticated:
        customer = request.user
        order,created = Order.objects.get_or_create(customer = customer,complete = False)
        items = order.orderitem_set.all()
        # COUNT
        cartItems = order.get_cart_items
    else:
        items =[]
        order = {'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    context = {'items':items,'order':order,'products':products,'cartItems':cartItems}
    return render(request,'app/home.html',context)


# CART
def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order,created = Order.objects.get_or_create(customer = customer,complete = False)
        items = order.orderitem_set.all()
        # COUNT
        cartItems = order.get_cart_items
    else:
        items =[]
        order = {'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items']
    context={'items':items,'order':order,'cartItems':cartItems}
    return render(request,'app/cart.html',context)


# CHECKOUT
def checkout(request):
    if request.user.is_authenticated:
                if request.method == 'POST':
                    shippingAddress=ShippingAddress()
                    consignee = request.POST.get('consignee')
                    email = request.POST.get('email')
                    address = request.POST.get('address')
                    city = request.POST.get('city')
                    state = request.POST.get('state')
                    phone = request.POST.get('phone')
                    shippingAddress.consignee=consignee
                    shippingAddress.email=email
                    shippingAddress.address=address
                    shippingAddress.city=city
                    shippingAddress.state=state
                    shippingAddress.phone=phone
                    shippingAddress.save()
                    return redirect('home')
                customer = request.user
                order,created = Order.objects.get_or_create(customer = customer,complete = False)
                items = order.orderitem_set.all()
                # COUNT
                cartItems = order.get_cart_items
    else:
                items =[]
                order = {'get_cart_items':0,'get_cart_total':0}
                cartItems = order['get_cart_items']
    context={'items':items,'order':order,'cartItems':cartItems,}
    return render(request,'app/checkout.html',context)


# DETAIL
def detail(request):
    if request.user.is_authenticated:
        customer = request.user
        order,created = Order.objects.get_or_create(customer = customer,complete = False)
        items = order.orderitem_set.all()
        # COUNT
        cartItems = order.get_cart_items
    else:
        items =[]
        order = {'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items']
    id = request.GET.get('id','')
    products = Product.objects.filter(id =id)
    # COMMENT-------
    item_details = Product.objects.get(id=int(id))
    userview = request.user
    if request.method == 'POST':
        star_rating = request.POST.get('rating')
        item_review = request.POST.get('item_review')
        item_reviews = Review(userview=userview, item=item_details, rating=star_rating, review_desp = item_review)
        item_reviews.save()
        rating_details = Review.objects.filter(item=item_details)
    rating_details = Review.objects.filter(item=item_details)
    context={'products':products,'items':items,'order':order,'cartItems':cartItems,'reviews': rating_details}
    return render(request,'app/detail.html',context)



# SEARCH
def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        checks = Product.objects.filter(name__contains = searched)
    # COUNT CART
    if request.user.is_authenticated:
        customer = request.user
        order,created = Order.objects.get_or_create(customer = customer,complete = False)
        items = order.orderitem_set.all()
        # COUNT
        cartItems = order.get_cart_items
    else:
        items =[]
        order = {'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
   
    return render(request,'app/search.html',{'searched' : searched,'checks' : checks,'products':products,'cartItems':cartItems})



# add vs remove
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user
    product = Product.objects.get(id = productId)
    order,created = Order.objects.get_or_create(customer = customer,complete = False)
    orderItem,created = OrderItem.objects.get_or_create(order = order,product = product)
    if action == 'add':
        orderItem.quantity +=1
    elif action == 'remove':
        orderItem.quantity -=1
    orderItem.save()
    if orderItem.quantity <=0:
        orderItem.delete()
    return JsonResponse('added',safe=False)

# Product
def pc(request):
    if request.user.is_authenticated:
        customer = request.user
        order,created = Order.objects.get_or_create(customer = customer,complete = False)
        items = order.orderitem_set.all()
        # COUNT
        cartItems = order.get_cart_items
    else:
        items =[]
        order = {'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    context = {'products':products,'cartItems':cartItems}
    return render(request,'app/pc.html',context)

def phone(request):
    if request.user.is_authenticated:
        customer = request.user
        order,created = Order.objects.get_or_create(customer = customer,complete = False)
        items = order.orderitem_set.all()
        # COUNT
        cartItems = order.get_cart_items
    else:
        items =[]
        order = {'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    context = {'products':products,'cartItems':cartItems}
    return render(request,'app/phone.html',context)

def laptop(request):
    if request.user.is_authenticated:
        customer = request.user
        order,created = Order.objects.get_or_create(customer = customer,complete = False)
        items = order.orderitem_set.all()
        # COUNT
        cartItems = order.get_cart_items
    else:
        items =[]
        order = {'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    context = {'products':products,'cartItems':cartItems}
    return render(request,'app/laptop.html',context)

def edit(request):
    if request.user.is_authenticated:
        customer = request.user
        if request.method == "POST":
            customer.username = request.POST.get('username')
            customer.email = request.POST.get('email')
            customer.first_name = request.POST.get('first_name')
            customer.last_name = request.POST.get('last_name')
            customer.password1 = request.POST.get('password1')
            customer.password2 = request.POST.get('password2')
            customer.save()
            messages.success(request, "Product Updated Successfully")
            return redirect('/')
        order,created = Order.objects.get_or_create(customer = customer,complete = False)
        # COUNT
        cartItems = order.get_cart_items
    else:
        items =[]
        order = {'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    context = {'products':products,'cartItems':cartItems}
    return render(request,'app/edit.html',context)




# VIEW VIEW  

# View Home
def viewhome(request):
    products = Product.objects.all()
    context ={'products':products}
    return render(request,'view/viewhome.html',context)


# Product
def viewpc(request):
    products = Product.objects.all()
    context ={'products':products}
    return render(request,'view/viewpc.html',context)

def viewphone(request):
    products = Product.objects.all()
    context ={'products':products}
    return render(request,'view/viewphone.html',context)

def viewlaptop(request):
    products = Product.objects.all()
    context ={'products':products}
    return render(request,'view/viewlaptop.html',context)

def viewsearch(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        checks = Product.objects.filter(name__contains = searched)
    products = Product.objects.all()
   
    return render(request,'view/viewsearch.html',{'searched' : searched,'checks' : checks,'products':products,})


