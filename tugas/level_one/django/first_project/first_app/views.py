from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import ShoesType, Shoes, OwnerRecord

# Create your views here.
def index(request):
    owner_list = OwnerRecord.objects.order_by("date")
    context = {"owner_records": owner_list}
    return render(request, "first_app/index.html", context=context)