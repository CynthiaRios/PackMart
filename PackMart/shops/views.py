from django import forms
from django.contrib import auth
from django.http import Http404, HttpResponseRedirect, JsonResponse,HttpResponse,StreamingHttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .forms import ShopForm, NewUserForm, ProductForm
from .models import Shop, Product, Review, Tokens

def index(request):
    return render(request, 'welcome.html')

# accounts and tokens
def login(request):
    if request.user.is_authenticated():
        return redirect('admin_page')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            index(request)
        #else:
            #messages.error(request, 'Error wrong username/password')
    return render(request, 'welcome.html')

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            index(request)
        #messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="registration/register.html", context={"register_form":form})

def logout(request):
    auth.logout(request)
    return render(request,'welcome.html')

#shops
@login_required
def shop_create(request):
    user = request.user
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            shop = Shop(
                name=form.cleaned_data['name'],
                business_type = form.cleaned_data['business_type'],
                product_type = form.cleaned_data['product_type'],
                service_type = form.cleaned_data['service_type'],
                description = form.cleaned_data['description'],
                logo = form.cleaned_data['logo'],
                banner_image = form.cleaned_data['banner_image'],
                owner = user
            )
            shop.save()
            return render
            (request,
            'shop/read.html',
            {'shop':shop}
            )
    else:
        form = ShopForm()
    return render(
        request,
        'shop/form.html',
        {'form': form}
    )

@login_required
def shop_list(request):#, type=None, filter=None):
    context = {}
    #if type != None and filter != None:
    #    if type == "service":
    #        context['shops']= Shop.objects.filter(service_type = filter)
    #    else:
    #        context['shops']= Shop.objects.filter(business_type = filter)
    if request.GET:
        name = request.GET.get('name', '')
        #business_type = request.GET.get('business_type', None)
        #service_type = request.GET.getlist('service_type', None)
        #product_list = request.GET.getlist('product_type', None)
        ########
        shops=sorted(get_shop_queries(name))
        context['shops']= shops
    else:
        context['shops']= Shop.objects.all().order_by('name')
    return render(
        request,
        'shop/list.html',
        context
    )

@login_required
def my_shop_list(request):#, type=None, filter=None):
    context = {}
    #if type != None and filter != None:
    #    if type == "service":
    #        context['shops']= Shop.objects.filter(service_type = filter)
    #    else:
    #        context['shops']= Shop.objects.filter(business_type = filter)
    context['shops']= Shop.objects.filter(owner=request.user)
    return render(
        request,
        'shop/list.html',
        context
    )

def get_shop_queries(name=None):#, business_type=None, service_type=None, product_list=None):
    queryset = []
    queries = name.split(" ")
    for q in queries:
        shops = Shop.objects.filter(
            Q(name__icontains=q) | Q(description__icontains=q) | Q(service_type__icontains=q) |Q(business_type__icontains=q) | Q(product_type__icontains=q)
        ).filter().distinct()
    #if business_type:
    #    shops = shops.filter(
    #        Q(business_type=(business_type))
    #    )
    #if service_type != None:
    for Shop in shops:
        queryset.append(Shop)
    return list(set(queryset))

@login_required
def shop_read(request, id):
    shop = Shop.objects.get(pk=id)
    products = Product.objects.filter(shop = shop)
    if request.GET:
        name = request.GET.get('name', '')
        description = request.GET.get('description', None)
        image = request.GET.get('image', None)
        if name and description:
            product_create(name, description, shop, image)
    if request.POST:
        name = request.POST.get('name', '')
        description = request.POST.get('description', None)
        banner_image = request.POST.get('image', None)
        if name:
            shop.name = name
        if description:
            shop.description = description
        if banner_image:
            shop.banner_image = banner_image
        shop.save()
    return render(request, 'shop/read.html', { 'shop': shop, 'products':products,'owner':shop.owner })

@login_required
def shop_update(request, id):
    shop = Shop.objects.get(pk=id)
    products = Product.objects.filter(shop = shop)
    if shop.owner != request.user:
        return render(request, 'shop/read.html', { 'shop': shop, 'products':products,'owner':shop.owner })
    else:
        if shop.owner != request.user:
            return render(request, 'shop/read.html', { 'shop': shop, 'products':products,'owner':shop.owner })

#products
def product_create(name, description, shop, image=None):
    product = Product(
        name = name,
        description = description,
        image = image,
        shop = shop
    )
    product.save()
    return render
    (request,
    'shop/read.html',
    {'shop':shop}
    )


@login_required
def product_read(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'product/read.html', { 'product': product })
