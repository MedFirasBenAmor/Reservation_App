from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.views.decorators.csrf import csrf_protect
from .models import Reservation

# Create your views here.
from django.http import HttpResponse
from .models import User
def home(request):
    return HttpResponse("Hello, Django!")
@login_required
def home_page(request):
    return render(request, 'reservationapp/home_page.html')

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
    return render(request, 'reservationapp/index.html')
def sign_view(request):
    return render(request, 'reservationapp/sign.html')
def nav_view(request):
    return render(request, 'reservationapp/nav.html')
@csrf_protect
def index_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
    return render(request, 'reservationapp/index.html')
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'reservationapp/register.html', {'form': form})
def user_list(request):
    users = User.objects.all()
    return render(request, 'reservationapp/user_list.html', {'users': users})
@login_required
def make_reservation(request):
    if request.method == 'POST':
        date = request.POST['date']
        time = request.POST['time']
        
        # Check for existing reservations at the same date and time
        existing_reservation = Reservation.objects.filter(
            date=date,
            time=time
        ).exists()
        
        if existing_reservation:
            return render(request, 'reservationapp/make_reservation.html', {
                'error_message': 'Please try to choose another time, the server is reserved.'
            })
            
        reservation = Reservation(
            user=request.user,
            date=date,
            time=time,
            guests=request.POST['guests'],
            special_requests=request.POST['special_requests']
        )
        reservation.save()
        return redirect('view_reservations')
    return render(request, 'reservationapp/make_reservation.html')

@login_required
def view_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservationapp/view_reservations.html', {'reservations': reservations})


