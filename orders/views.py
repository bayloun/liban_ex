from django.shortcuts import render, redirect
from orders.forms import *
from areas.models import Zone
from orders.models import Order
from driver.models import Driver
from seller.models import Seller
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from financials.models import Financial
from areas.models import Location
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def entry(request):
    form = OrderForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, 'Order successfully created.')
            order = form.save()
            order.date_received = request.POST["date_received"] + " " + str(timezone.now().time())
            order.save()
    return render(request, 'orders/entry.html', {'form': form})

@login_required
def assign(request):
    zones = Zone.objects.all()
    drivers = Driver.objects.all()

    zone = request.GET.get("zone")
    if zone != "" and zone != None:
        zone = Zone.objects.get(zone=zone)
        orders = Order.objects.filter(zone=zone)

        page = request.GET.get('page', 1)
        paginator = Paginator(orders, 50)
        try:
            orders = paginator.page(page)
        except PageNotAnInteger:
            orders = paginator.page(1)
        except EmptyPage:
            orders = paginator.page(paginator.num_pages)

    else:
        orders = None

    if request.method == "POST":
        if request.POST.get("driver"):
            driver = Driver.objects.get(id=request.POST["driver"])
            orders = request.POST.getlist("selected_order")
            for order in orders:
                x = Order.objects.get(id=order)
                x.driver = driver
                x.save()
            messages.add_message(request, messages.SUCCESS, 'Your selected orders have been assigned to ' + str(driver))
            return redirect("/order/assign")

    return render(request, 'orders/assign.html', {"orders": orders, "zones": zones, "drivers": drivers, "selected": zone})

@login_required
def update(request):
    order = Order.objects.get(id=request.POST["order_id"])
    location = Location.objects.get(id=request.POST["location"])
    order.location = location
    order.actual_usd = float(request.POST["actual_dollars"])
    order.actual_lebanese = float(request.POST["actual_lebanese"])
    order.save()
    return HttpResponse('success')

@login_required
def search(request):
    seller = request.GET.get("seller", False)
    zone = request.GET.get("zone", False)
    location = request.GET.get("location", False)
    financial = request.GET.get("financial", False)

    orders = Order.objects.all()
    sellers = Seller.objects.all()
    zones = Zone.objects.all()
    locations = Location.objects.all()
    financials = Financial.objects.all()

    if request.method == "POST":
        number = request.POST["number"]
        order = Order.objects.filter(order_id=number)

        return render(request, "orders/search.html", {"orders": order, "sellers": sellers, "zones" : zones, "locations": locations, "financials": financials})

    else:
        if seller:
            seller = Seller.objects.get(id=seller)
            orders = orders.filter(seller=seller)

        selected_seller = seller

        if zone:
            zone = Zone.objects.get(id=zone)
            orders = orders.filter(zone=zone)

        selected_zone = zone

        if location:
            location = Location.objects.get(id=location)
            orders = orders.filter(location=location)

        selected_location = location

        if financial:
            financial = Financial.objects.get(id=financial)
            orders = orders.filter(financial_status=financial)

        selected_financial = financial

        return render(request, "orders/search.html", {"orders": orders, "sellers": sellers, "zones" : zones, "locations": locations, "financials": financials, "selected_seller": selected_seller, "selected_zone": selected_zone, "selected_location": selected_location, "selected_financial": selected_financial})
