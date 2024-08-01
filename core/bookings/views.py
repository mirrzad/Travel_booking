from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Trip
from .forms import TripForm
from django.contrib import messages
from django.views.generic import DeleteView


class TripListView(View):
    template_name = 'bookings/list_trips.html'

    def get(self, request):
        trips = Trip.objects.all()
        return render(request, self.template_name, {'trips': trips})


class TripCreateView(View):
    template_name = 'bookings/create_trip.html'
    form_class = TripForm

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Trip.objects.create(
                destination=cd['destination'],
                departure_date=cd['departure_date'],
                return_date=cd['return_date'],
                number_of_travelers=cd['number_of_travelers'],
            )
            messages.success(request, 'Your trip has been successfully booked.', 'success')
            return redirect('bookings:list_trip')
        return render(request, self.template_name, {'form': form})


class TripUpdateView(View):
    form_class = TripForm
    template_name = 'bookings/update_trip.html'

    def setup(self, request, *args, **kwargs):
        self.trip_instance = get_object_or_404(Trip, id=kwargs['pk'])
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        trip = self.trip_instance
        form = self.form_class(instance=trip)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        trip = self.trip_instance
        form = self.form_class(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your trip has been successfully edited', 'success')
            return redirect('bookings:list_trip')
        return render(request, self.template_name, {'form': form})


class TripDeleteView(View):
    template_name = 'bookings/confirm_delete.html'

    def setup(self, request, *args, **kwargs):
        self.trip_instance = get_object_or_404(Trip, id=kwargs['pk'])
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        trip = self.trip_instance
        return render(request, self.template_name, {'trip': trip})

    def post(self, request, *args, **kwargs):
        trip = self.trip_instance
        trip.delete()
        messages.success(request, 'Your trip has been successfully deleted', 'success')
        return redirect('bookings:list_trip')
