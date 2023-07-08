from django.urls import path
from .views import (
    RoomListView,
    BookingList,
    RoomDetailView,
    BookingView
)


app_name = 'hotel'

urlpatterns = [
    path('', RoomListView, name='RoomList'),
    path('room/<category>/', RoomDetailView.as_view(), name='RoomDetailView'),
    path('booking_list/', BookingList.as_view(), name='RoomList'),
    path('booking/', BookingView.as_view(), name='BookingView')
]