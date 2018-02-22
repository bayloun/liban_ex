from django.shortcuts import render
from driver.models import Driver
from orders.models import Order
from financials.models import Financial

# Create your views here.

def checkin(request):
    orders = None
    selected_driver = None
    total_owed = None
    drivers = Driver.objects.all()
    statuses = Financial.objects.all()
    if request.method == "POST":
        driver = Driver.objects.get(id=request.POST["driver"])
        selected_driver = driver
        orders = Order.objects.filter(driver=driver)
        total_owed = 0
        for order in orders:
            if order.actual_amount_usd:
                total_owed += order.actual_amount_usd
    return render(request, "driver/checkin.html", {"drivers": drivers, "selected_driver": selected_driver, "orders": orders, "statuses": statuses, "total_owed": total_owed})
