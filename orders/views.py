from django.shortcuts import render, redirect
from orders.forms import *
from areas.models import Zone
from orders.models import Order
from driver.models import Driver
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from financials.models import Financial
from areas.models import Location
from django.http import HttpResponse

# Create your views here.

def entry(request):
    form = OrderForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Order successfully created.')
    return render(request, 'orders/entry.html', {'form': form})

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


def update(request):
    order = Order.objects.get(id=request.POST["order_id"])
    location = Location.objects.get(id=request.POST["location"])
    order.location = location
    order.actual_usd = float(request.POST["actual_dollars"])
    order.actual_lebanese = float(request.POST["actual_lebanese"])
    order.save()
    return HttpResponse('success')
