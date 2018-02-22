from django.shortcuts import render
from driver.models import Driver
from orders.models import Order
from financials.models import Financial
from areas.models import Location

# Create your views here.

def checkin(request):
    orders = None
    selected_driver = None
    total_owed = None
    drivers = Driver.objects.all()
    locations = Location.objects.all()
    if request.method == "POST":
        driver = Driver.objects.get(id=request.POST["driver"])
        selected_driver = driver
        orders = Order.objects.filter(driver=driver)
        total_owed = 0
        for order in orders:
            if order.actual_usd:
                total_owed += order.actual_usd
    return render(request, "driver/checkin.html", {"drivers": drivers, "selected_driver": selected_driver, "orders": orders, "locations": locations, "total_owed": total_owed})
