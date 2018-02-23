from django.shortcuts import render
from areas.models import Location
from seller.models import Seller
from orders.models import Order
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def search(request):
    sellers = Seller.objects.all()
    locations = Location.objects.all()
    if request.method == "POST":
        seller = Seller.objects.get(id=request.POST["seller"])
        if not request.POST.get("location"):
            orders = Order.objects.filter(seller=seller)
            selected_seller = seller
            selected_location = None
        else:
            location = Location.objects.get(id=request.POST["location"])
            orders = Order.objects.filter(seller=seller, location=location)
            selected_seller = seller
            selected_location = location
        return render(request, "seller/search.html", {"sellers": sellers, "locations": locations, "orders": orders, "selected_seller": selected_seller, "selected_location": selected_location})
    return render(request, "seller/search.html", {"sellers": sellers, "locations": locations})
