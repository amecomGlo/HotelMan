from django.urls import path
from .views import (
    RoomListView,
    BookingListView,
    RoomDetailView,
    BookingView,
    CancelRoomView
)


app_name = 'hotel'

urlpatterns = [
    path('', RoomListView, name='RoomList'),
    path('room/<category>/', RoomDetailView.as_view(), name='RoomDetailView'),
    path('booking_list/', BookingListView.as_view(), name='Booking_List'),
    path('booking/', BookingView.as_view(), name='BookingView'),
    path('booking/cancel/<pk>/', CancelRoomView.as_view(), name='CancelRoomView')
]