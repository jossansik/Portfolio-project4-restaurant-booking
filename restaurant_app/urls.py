from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('menu/foodmenu/', views.FoodMenuView.as_view(), name='food_menu'),
    path('menu/drinksmenu/', views.DrinksMenuView.as_view(), name='drinks_menu'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('booking/', login_required(views.BookingView.as_view()), name='booking'),
    path('booking/details/', login_required(views.BookingDetailsView.as_view()),
         name='booking_details'),
    path('booking/complete/', login_required(views.BookingCompleteView.as_view()),
         name='booking_complete'),
    path('my/reservation/', login_required(views.MyReservationView.as_view()),
         name='my_reservation'),
]
