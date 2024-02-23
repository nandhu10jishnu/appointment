from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Departments, Doctors
from .models import Booking
from .forms import BookingForm
from .filters import BookingFilter
#from .views import BookingListView

 
def booking(request):
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')

    dict_form = {
        'form': form
    }
    return render(request, 'booking.html', dict_form)
# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
     return render(request, "about.html")


def doctors(request):
    dict_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(request, 'doctors.html', dict_docs)

def contact(request):
     return render(request, "contact.html")

def department(request):
    dict_dept = {
        'dept': Departments.objects.all()
    }
    return render(request, 'department.html', dict_dept)

class BookingListView(ListView):
    model = Booking
    template_name = 'booking_list.html'
    context_object_name = 'bookings'
    filterset_class = BookingFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context