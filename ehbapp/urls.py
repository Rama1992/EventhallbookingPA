from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="ehbhome.html"),
    path('home/', views.loginview, name="a_base.html"),
    path('halls/', views.eventhall_list, name="hall_list"),
    path('halls/add', views.hall_addhall, name="add_eventhalls"),
    path('halls/<int:pk>/edit', views.hall_edithall, name="edit_eventhalls"),
    path('halls/<int:pk>/delete', views.hall_deletehall, name="delete_eventhalls"),
    path('halls/<int:pk>/', views.eventhall_detail, name="hall_detail"),
    path('halls/reserve/<int:pk>', views.hall_reserve, name="booking"),
    path('halls/reserve/<int:pk>/edit', views.hall_editbooking, name="hall_editbooking"),
    path('halls/reserve/<int:pk>/delete', views.hall_deletebooking, name="hall_deletebooking"),
    path('halls/bookings', views.hall_bookings, name='hall_bookings')
]