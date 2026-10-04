from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path(
        'api/menu-items/',
        views.MenuItemsView.as_view(),
        name='menu-items'
    ),

    path(
        'api/menu-items/<int:pk>/',
        views.SingleMenuItemView.as_view(),
        name='single-menu-item'
    ),

    path(
        'api/bookings/',
        views.BookingView.as_view(),
        name='bookings'
    ),

    path(
        'api/bookings/<int:pk>/',
        views.SingleBookingView.as_view(),
        name='single-booking'
    ),
]