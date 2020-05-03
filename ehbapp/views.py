from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response

from ehbapp.forms import BookingForm, BookingEditForm, AddEventHall
from ehbapp.models import EventHall, Reservations
from django.contrib.auth.decorators import login_required
from ehbapp.decorators import employee_required, customer_required
from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms import UserLoginForm
from accounts.models import CustomUser
import datetime


# Create your views here.
def home(request):
    return render(request, 'ehbhome.html')


@login_required()
def loginview(request):
    return render(request, 'base.html')


def eventhall_list(request):
    halls_list = EventHall.objects.all()
    context = {
        'halls': halls_list
    }
    return render(request, 'hall_list.html', context)


def eventhall_detail(request, pk):
    hall = EventHall.objects.get(pk=pk)
    context = {
        'hall': hall
    }
    return render(request, 'hall_detail.html', context)
    # if request.method == 'GET':
    #     form = BookingForm()
    #     hall = EventHall.objects.get(pk=pk)
    #     context = {
    #         'hall': hall,
    #         'form': form
    #     }
    #     return render(request, 'hall_detail.html', context)


@login_required()
def hall_reserve(request, pk):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = BookingForm()
            # print('hall_id'EventHall.objects.get(id=pk))
            context = {
                'form': form
            }
            return render(request, 'booking.html', context)
        elif request.method == 'POST' and 'book' in request.POST:
            form = BookingForm(request.POST)
            if form.is_valid():
                hall = EventHall.objects.get(pk=pk)
                user = request.user
                booking = Reservations()
                booking.booked_customer_Name = CustomUser.objects.get(username=user)
                booking.booked_on_date = form.cleaned_data['booked_on_date']
                # booking.booked_on_date = request.POST.get['date']
                # booking.booked_hall_id = EventHall.objects.get(id=pk)
                booking.booked_hall_name = EventHall.objects.get(id=pk)
                booking.save()
                print(booking.booked_hall_name)
                reservations = Reservations.objects.filter(booked_customer_Name=user)
                context = {
                    'reservations': reservations
                }
                return render(request, 'hall_bookings.html', context)


def hall_bookings(request):
    user = request.user
    customer_Name = CustomUser.objects.get(username=user)
    print(user.get_all_permissions())
    if user.is_active and user.is_superuser:
        reservations = Reservations.objects.all()
    elif user.is_active:
        reservations = Reservations.objects.filter(booked_customer_Name=customer_Name)
    context = {
        'reservations': reservations
    }
    return render(request, 'hall_bookings.html', context)


def hall_editbooking(request, pk):
    booking = get_object_or_404(Reservations, pk=pk)
    form = BookingEditForm(instance=booking)
    user = request.user
    print(request.method)
    if request.method == 'POST' and 'update' in request.POST:
        booking = get_object_or_404(Reservations, pk=pk)
        form = BookingEditForm(request.POST, instance=booking)
        print(booking)
        if form.is_valid():
            print('inside post')
            booking.booked_on_date = form.cleaned_data['booked_on_date']
            booking.save()
            reservations = Reservations.objects.filter(booked_customer_Name=user)
            context = {
                'reservations': reservations
            }
            return render(request, 'hall_bookings.html', context)
    elif request.method == 'GET':
        form = BookingEditForm(instance=booking)
        return render(request, 'hall_editbooking.html', {'form': form})


def hall_deletebooking(request, pk):
    booking = get_object_or_404(Reservations, pk=pk)
    booking.delete()
    return redirect('hall_bookings')


def hall_addhall(request):
    form = AddEventHall(request.POST or None)
    if form.is_valid() and 'savehall' in request.POST:
        form = form.save(commit=False)
        form.save()
        halls_list = EventHall.objects.all()
        context = {
            'halls': halls_list
        }
        return render(request, 'hall_list.html', context)
    else:
        form = AddEventHall()
    return render(request, 'add_eventhalls.html', {'form': form})


def hall_edithall(request, pk):
    hall = get_object_or_404(EventHall, pk=pk)
    if request.method == 'POST' and 'edithall' in request.POST:
        edit_form = AddEventHall(request.POST, instance=hall)
        if edit_form.is_valid():
            hall = edit_form.save()
            hall.save()
            halls_list = EventHall.objects.all()
            context = {
                'halls': halls_list
            }
            return render(request, 'hall_list.html', context)
    else:
        edit_form = AddEventHall(instance=hall)
    return render(request, 'edit_eventhalls.html', {'form': edit_form})


def hall_deletehall(request, pk):
    hall = get_object_or_404(EventHall, pk=pk)
    hall.delete()
    return redirect('hall_list')