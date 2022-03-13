"""URLs for the booking app."""
from django.urls import path

from . import views

app_name = 'booking'
urlpatterns = [
    path('(<pk>\d+)/',
        views.BookingDetailView.as_view(),
        name='booking_detail'),
    path('create/',
        views.BookingCreateView.as_view(),
        name='booking_create'),
    path(r'', views.BookingListView.as_view(), name='booking_list'),
]
