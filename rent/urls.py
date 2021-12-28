from django.urls import path
from rent.views import location_view, rent_view, user_view, booking_view, auth_view, dashboard_view

urlpatterns = [
    path('dashboard/', dashboard_view.DashboardView.as_view(), name='dashboard'),
    # Location
    path('location/', location_view.LocationListView.as_view(), name='location_listview'),
    path('location-create/', location_view.LocationCreateView.as_view(), name='location_create'),
    path('location-update/<pk>/', location_view.LocationUpdateView.as_view(), name='location_update'),
    path('location-delete/<pk>/', location_view.LocationDeleteView.as_view(), name='location_delete'),
    # Rent
    path('rent/', rent_view.RentListView.as_view(), name='rent_listview'),
    path('create-rent/', rent_view.CreateRentView.as_view(), name='create_rent'),
    path('rent-update/<pk>/', rent_view.RentUpdateView.as_view(), name='rent_update'),
    path('rent-detail/<pk>/', rent_view.RentDetailsView.as_view(), name='rent_details'),
    path('rent-delete/<pk>/', rent_view.RentDeleteView.as_view(), name='rent_delete'),
    # User
    path('users/', user_view.UserListView.as_view(), name='use_list'),
    path('user-update/<pk>/', user_view.UserUpdateView.as_view(), name='use_update'),
    path('users-delete/<pk>/', user_view.UserDeleteView.as_view(), name='use_delete'),
    path('profile', auth_view.ProfileView.as_view(), name='profile'),
    path('profile-update/<pk>/', auth_view.ProfileUpdateView.as_view(), name='profile_update'),
    # Booking
    path('booking/', booking_view.AddNewBookingView.as_view(), name='booking'),
    path('new-booking/', booking_view.NewBookingView.as_view(), name='new_booking'),
    path('all-booking/', booking_view.AllBookingView.as_view(), name='all_booking'),
    path('my-booking-history/', booking_view.MyBookingHistory.as_view(), name='my_booking_history'),
    path('booking-confirm/<pk>/', booking_view.UpdateBookingView.as_view(), name='booking_confirm'),
    path('booking-delete/<pk>/', booking_view.DeleteBookingView.as_view(), name='booking_delete'),
    # Authentication
    path('login/', auth_view.SignInView.as_view(), name='login'),
    path('logout/', auth_view.Logout.as_view(), name='logout'),
    path('registration/', auth_view.SingUpView.as_view(), name='registration'),
]
