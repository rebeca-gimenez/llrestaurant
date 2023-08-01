from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Menu
from django.views import generic
from llrestaurant.forms import ReservationForm

# Create your views here.
def home(request):
    return render(request, "llrestaurant/index.html")

def about(request):
    return render(request, "llrestaurant/about.html")
    
def menu(request):
    dish_list = Menu.objects.all()
    template = loader.get_template("llrestaurant/menu.html")
    context = { "dish_list": dish_list,
    }
    return HttpResponse(template.render(context, request))

class ItemDetails(generic.DetailView):
    model = Menu
    template_name = "llrestaurant/menu_item.html"

def reservations(request):
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, "llrestaurant/reservations.html", context)

def thankyou(request):
    return render(request, "llrestaurant/typ.html")